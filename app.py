__author__ = 'Erdam Techera, Rodrigo Gabín, Lorena Gallas, Valentina Peña, Erika Poses'


import bcrypt
import werkzeug
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
import MySQLdb.cursors
from formulario import RegistroForm
#from flask.ext.bcrypt import Bcrypt
from flask_login import login_manager
import os

carpeta=os.path.abspath('/freebooks/static/_img/fotoUser')
carpeta2=os.path.abspath('/freebooks/static/_img/fotos')

permitidas = { 'png', 'jpg', 'jpeg', 'gif'}

app=Flask(__name__)

#configuración imagenes
app.config['UPLOAD_FOLDER'] =carpeta
app.config['UPLOAD_FOLDER2'] =carpeta2

#fin configuración imagenes
#configuración clave secreta
app.config['SECRET_KEY']='9acA0Zr98j/3yX erdam!jmN]LWX/,?RTc07fab47dc7770'
#fin clave secreta
#configuración de servidor
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='freebooks'
mysql=MySQL(app)
#fin de configuración de mi servidor

#----------construcción.html------------------------------
@app.route('/construccion')
def construccion():
    return render_template('construccion.html', Titulo='-Construcción')

#----------index.html------------------------------
@app.route('/', methods=['GET'] )
@app.route('/index', methods=['GET'])
def index():
    if 'username' in session:
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM  libro WHERE libro_id  not in (SELECT libro_id FROM likee WHERE usuario_id=(%s))',(session['id'],))
        data=list(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        if len(data)>0:
             return render_template('index.html',libros=data, Titulo='_index')
        return render_template('index.html', Titulo='_index')
    return render_template('presentacion.html',Titulo='_login' )

#----------perfil.html------------------------------

@app.route('/perfil',  methods=['GET'])
def perfil():
    if 'username' in session:
        return render_template('perfil.html', Titulo='_perfil')
    return render_template('login.html', Titulo='_login')

#----------chat.html------------------------------

@app.route('/chat')
def chat():
    if 'username' in session:
       return render_template('chat.html', Titulo='-chat')
    return render_template('login.html', Titulo='_login')

#----------libro.html------------------------------

@app.route('/libro')
def libro():
    if 'username' in session:
      return redirect(url_for('listar_libros'))
    return render_template('login.html', Titulo='_login')

#----------calificacion.html-----------------------------

@app.route('/calificaciones')
def calificaciones():
    if 'username' in session:
        return render_template('calificaciones.html',Titulo='-calificaciones')
    return render_template('login.html', Titulo='_login')

#--------------registro----------------------

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    if session.get('loggedin'):
        return redirect(url_for('index'))
    else:
        form=RegistroForm()
        if form.validate_on_submit():
            usuario=form.User_nick.data
            email=form.User_email.data
           # password=form.User_pass.data.encode('utf-8')
            #passw =bcrypt.hashpw(password, bcrypt.gensalt())
            passw=form.User_pass.data
            cur=mysql.connection.cursor()
            sql = "INSERT INTO usuario(usuario_email, usuario_nick, usuario_pass) VALUES (%s, %s, %s)"
            val = (email, usuario,passw)
            cur.execute(sql, val)
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('login'))
        return render_template('registro.html', Titulo='_registro', form=form)
    return render_template('index.html', Titulo='_index')

#----------Login------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
       # password = request.form['password'].encode('utf-8')
       # passw = bcrypt.hashpw(password, bcrypt.gensalt())
        passw =request.form['password']
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute('SELECT * FROM usuario WHERE usuario_email = %s AND usuario_pass = %s', (email, passw,))
        usuario = curl.fetchone()
        curl.close()
        if usuario:
            session['loggedin'] = True
            session['id'] = usuario['usuario_id']
            session['username'] = usuario['usuario_nick']
            session['activo'] = usuario['usuario_activo']
            session['email'] = usuario['usuario_email']
            session['foto'] = usuario['usuario_foto']
            session['nombre'] = usuario['usuario_nom']
            session['apellido'] = usuario['usuario_ape']
            session['nombre2'] = usuario['usuario_nom2']
            session['apellido2'] = usuario['usuario_ape2']
            session['naci'] = usuario['usuario_cumple']
            session['pais'] = usuario['usuario_pais']
            session['departamento'] = usuario['usuario_dep']
            session['direccion'] = usuario['usuario_direccion']
            session['direcNumero'] = usuario['usuario_num']
            session['direcAp'] = usuario['usuario_ap']
            session['cp'] = usuario['usuario_cp']
            session['prefijo'] = usuario['usuario_pre']
            session['cel'] = usuario['usuario_cel']
            session['cel2'] = usuario['usuario_cel2']
            session['email2'] = usuario['usuario_email2']

            msg = 'Logueado'
            if session['activo']==1:
               return redirect(url_for('index'))
            else:
               return render_template('perfil.html', Titulo=msg)
        else:
             # Account doesnt exist or username/password incorrect
             msg = 'Incorrect username/password!'
             # Show the login form with message (if any)
    return render_template('login.html', Titulo=msg)

#----------Logout------------------------------
@app.route('/logout', methods=["GET", "POST"])
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('foto', None)
   session.pop('email', None)
   session.pop('activo', None)
   session.pop('nombre', None)
   session.pop('apellido', None)
   session.pop('nombre2', None)
   session.pop('apellido2', None)
   session.pop('naci', None)
   session.pop('pais', None)
   session.pop('departamento', None)
   session.pop('direccion', None)
   session.pop('direcNumero', None)
   session.pop('direcAp', None)
   session.pop('cp', None)
   session.pop('prefijo', None)
   session.pop('cel', None)
   session.pop('cel2', None)
   session.pop('email2', None)
   # Redirect to login page
   return redirect(url_for('login'))

#----------Datos------------------------------


def archivo_Permitico(archivo):
    return '.' in archivo and \
           archivo.rsplit('.', 1)[1].lower() in permitidas
#----------fucion Update-----------------------------
def update_sql(var, varSql):
    if var!='':
        cur = mysql.connection.cursor()
        primero="UPDATE usuario SET "
        segundo= "=%s WHERE usuario_id=%s "
        sql = primero + varSql + segundo
        val = (var,session['id'])
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return True
    return False
#----------Registro-----------------------------
@app.route('/datosUser', methods=['GET', 'POST'])
def upload_file():
    if 'username' in session:
        msj = ''
        if request.method == 'POST':

            if 'nom1' in request.form:
                    nom1 = request.form['nom1']
                    if(update_sql(nom1, 'user_nom')):
                        session['nombre'] =nom1
                        msj='Actualización exitosa!!!'
            if 'ape1' in request.form:
                    ape1 = request.form['ape1']
                    if(update_sql(ape1, 'user_ape')):
                        session['apellido']= ape1
                        msj = 'Actualización exitosa!!!'
            if request.method == 'POST':
                    nom2 = request.form['nom2']
                    if(update_sql(nom2, 'usuario_nom2')):
                        session['nombre2']=nom2
                        msj = 'Actualización exitosa!!!'
                    ape2 = request.form['ape2']
                    if(update_sql(ape2, 'usuario_ape2')):
                        session['apellido2']=ape2
                        msj = 'Actualización exitosa!!!'
                    cumple = request.form['cumple']
                    if(update_sql(cumple, 'usuario_cumple ')):
                        session['naci'] =cumple
                        msj = 'Actualización exitosa!!!'
                    pais = request.form['pais']
                    if(update_sql(pais, 'usuario_pais')):
                        session['pais']=pais
                        msj = 'Actualización exitosa!!!'
                    dep = request.form['dep']
                    if(update_sql(dep, 'usuario_dep ')):
                        session['departamento']=dep
                        msj = 'Actualización exitosa!!!'
                    loc = request.form['loc']
                    if(update_sql(loc, 'usuario_loc')):
                        msj = 'Actualización exitosa!!!'
                    dir = request.form['dir']
                    if(update_sql(dir, 'usuario_direccion')):
                        session['direccion'] =dir
                        msj = 'Actualización exitosa!!!'
                    num = request.form['num']
                    if(update_sql(num, 'usuario_num')):
                        session['direcNumero'] =num
                        msj = 'Actualización exitosa!!!'
                    apto = request.form['apto']
                    if(update_sql(apto, 'usuario_ap ')):
                        session['direcAp'] =apto
                        msj = 'Actualización exitosa!!!'
                    cp = request.form['cp']
                    if(update_sql(cp, 'usuario_cp ')):
                        session['cp'] = cp
                        msj = 'Actualización exitosa!!!'
                    prefijo = request.form['prefijo']
                    if(update_sql(prefijo,'usuario_pre ')):
                        session['prefijo']=prefijo
                        msj = 'Actualización exitosa!!!'
                    cel1 = request.form['cel1']
                    if(update_sql(cel1, 'usuario_cel')):
                        session['cel']=cel1
                        msj = 'Actualización exitosa!!!'
                    cel2 = request.form['cel2']
                    if(update_sql(cel2, 'usuario_cel2 ')):
                        session['cel2'] = cel2
                        msj = 'Actualización exitosa!!!'
                    email = request.form['email']
                    if(update_sql(email, 'usuario_email2')):
                        session['email2'] = email
                        msj = 'Actualización exitosa!!!'
                    cur = mysql.connection.cursor()
                    sql = "UPDATE usuario SET usuario_activo=1 WHERE usuario_nom!='sin datos' AND usuario_ape!='sin datos'"
                    cur.execute(sql)
                    mysql.connection.commit()
                    cur.close()
                    if 'img[0]' not in request.files:
                        msj = 'no hay archivo'
                        return msj
                    avatar =request.files['img[0]']
                    if avatar and archivo_Permitico(avatar.filename):
                        dirAvatar = secure_filename(avatar.filename)
                        avatar.save(os.path.join(app.config['UPLOAD_FOLDER'],session['username']+  dirAvatar))
                        direccion = '../static/_img/fotoUser/'+session['username']+dirAvatar
                        if(update_sql(direccion, 'usuario_foto ')):
                            session['foto'] = direccion
                            msj = 'Actualización exitosa!!!'

                    return render_template('perfil.html', msj=msj, Titulo='_perfil' )


    return render_template('login.html', Titulo='_login')

#----------función verifica archivo------------------------------
@app.route('/uploads/<archivo>')
def archivo_subido(archivo):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               archivo)
#----------------libros----------------------------------

@app.route('/listar_libros', defaults={'page':0})
@app.route('/listar_libros/page/<int:page>')
def listar_libros(page):
    if 'username' in session:
        perpage=8
        startat=page*perpage
        cur=mysql.connection.cursor()
        sql = 'SELECT * FROM libro WHERE usuario_id = %s LIMIT %s, %s'
        val = (session['id'],page,perpage)
        cur.execute(sql, val)
        data = list(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        return render_template('libro.html', libros = data)
    return render_template('login.html', Titulo='_login')


#----------------Eliminar---------------------------------
@app.route('/delete/<string:id>')
def delete(id):
    if 'username' in session:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM libro WHERE libro_id ={0}'.format(id))
        mysql.connection.commit()
        flash('Libro borrado satisfactoriamente')
        return redirect(url_for('listar_libros'))
    return render_template('login.html', Titulo='_login')

#----------------Eliminar2---------------------------------
@app.route('/delete2/<string:id>')
def delete2(id):
    if 'username' in session:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM likee WHERE libro_id={0}'.format(id))
        mysql.connection.commit()
        flash('Libro borrado satisfactoriamente')
        return redirect(url_for('listar_likes'))
    return render_template('login.html', Titulo='_login')

#----------------Editar---------------------------------
@app.route('/edit/<id>')
def get_libro(id):
    if 'username' in session:
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM  libro WHERE libro_id = %s',(id))
        data=cur.fetchall() #nos interesa el indice cero de esta lista, mi Usuario
        return render_template('plantilla.html', libro=data[0]) #envío de los datos al html
    return render_template('login.html', Titulo='_login')

#----------------Agregar----------------------------------

@app.route('/agregarBooks', methods=['POST'])
def agregarBooks():
    if 'username' in session:
        direccion1 =' ../static/_img/fotos/cronicas1.jpg'
        direccion2 =' ../static/_img/fotos/cronicas1.jpg'
        direccion3  =' ../static/_img/fotos/cronicas1.jpg'
        if 'titulo' in request.form:
            titulo='No existen datos'
        titulo = request.form['titulo']
        if 'autor' in request.form:
            autor='No existen datos'
        autor =request.form['autor']
        if not 'genero' in request.form:
            genero='No existen datos'
        genero = request.form.get('genero')


        if 'idioma' in request.form:
            idioma='No existen datos'
        idioma = request.form.get('idioma')


        if 'estado' in request.form:
            estado = 'No existen datos'
        estado = request.form.get('estado')

        if 'descripcion' in request.form:
            descripcion = 'No existen datos'
        descripcion = request.form.get('descripcion')


        # check if the post request has the file part

        avatar = request.files['img[1]']
        if avatar and archivo_Permitico(avatar.filename):
            dirAvatar = secure_filename(avatar.filename)
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER2'], session['username'] + dirAvatar))
            direccion1 = '../static/_img/fotos/' + session['username'] + dirAvatar


        avatar = request.files['img[2]']
        if avatar and archivo_Permitico(avatar.filename):
            dirAvatar = secure_filename(avatar.filename)
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER2'], session['username'] + dirAvatar))
            direccion2 = '../static/_img/fotos/' + session['username'] + dirAvatar


        avatar = request.files['img[3]']
        if avatar and archivo_Permitico(avatar.filename):
            dirAvatar = secure_filename(avatar.filename)
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER2'], session['username'] + dirAvatar))
            direccion3 = '../static/_img/fotos/' + session['username'] + dirAvatar

        cur = mysql.connection.cursor()
        sql = "INSERT INTO libro (titulo,autor,genero,idioma,estado,descripcion,foto1,foto2,foto3,usuario_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (titulo,autor,genero,idioma,estado,descripcion,direccion1,direccion2,direccion3,session['id'])
        cur.execute(sql, data)
        mysql.connection.commit()
        cur.close()
        msg = "Actualización exitosa!!!"
        return redirect(url_for('listar_libros'))

    return 'error'
#----------------like----------------------------------

@app.route('/likes',  methods=['GET'])
def likes():
    if 'username' in session:
        if request.method == 'GET':
            cur=mysql.connection.cursor()
            estado= request.args.get('gusta','')
            mi_libro=request.args.get('libro_id','')
            lik='INSERT INTO likee(libro_id, usuario_id, estado) VALUES (%s, %s, %s)'
            val = (mi_libro,session['id'], estado)
            cur.execute(lik, val)
            mysql.connection.commit()
            cur.close()
            return redirect('index')
    return render_template('login.html', Titulo='_login')

#----------------listar likes----------------------------------
@app.route('/listar_likes', defaults={'page':0})
@app.route('/listar_likes/page/<int:page>')
def listar_likes(page):
    if 'username' in session:
        perpage=8
        startat=page*perpage
        cur=mysql.connection.cursor()
        sql =""" SELECT * FROM libro WHERE libro_id  IN (SELECT libro_id FROM likee WHERE usuario_id = %s 
             AND estado = 1 ) LIMIT %s, %s"""
        val = ((session['id'], ), page, perpage )
        cur.execute(sql, val)
        #cur.execute('SELECT * FROM libros WHERE id IN (SELECT libro_id FROM likes WHERE estado=1 AND
        # user_id=%s)', (session['id'], ))# Alternativa 2
        data = list(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        return render_template('likes.html', libros = data)
    return render_template('login.html', Titulo='_login')

#----------------manejo error--------------------------------
@app.errorhandler(werkzeug.exceptions.NotFound)
def notfound(e):
    return 'Está tratando de acceder a un vínculo no existente', e.code

if __name__ == "__main__":
 app.run(debug=True, port=3000, threaded=True)