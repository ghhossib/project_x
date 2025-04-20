
from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from Controllers.GroupsController import GroupsController
from Controllers.StudentsController import StudentsController
from Controllers.UserController import UsersController

# создать объект класса Flask
application = Flask(__name__)
application.secret_key = 'la'
# для библиотеки login_manager добавил объект
# этот объект управляет авторизацией
login_manager = LoginManager(application)
@login_manager.user_loader
def user_loader(id):
    return UsersController.show(int(id))
# Маршрут главной страницы
# Добавить методы работы с данными POST и GET

@application.route('/', methods = ['POST', 'GET'])
def home():
    title = "Вход"
    message = ''


    #Проверка метода
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if UsersController.auth(login, password):
            #Создает сессию для пользователя который прошел аутентификацию
            user = UsersController.show_login(login)
            login_user(user)
            print(user)
            print(type(user.role_id))
            if current_user.role_id.id == 1:
                return redirect('/vhod')
            elif current_user.role_id.id == 2:
                return redirect('/teacher')
        else:
            message = 'Не верный логин или пароль'
    return render_template('index.html',
                           title = title,
                           message = message
                           )

@application.route('/registracia', methods = ['POST', 'GET'])
def registration_site():
    title = 'Регистрация'
    message = ''
    if request.method == 'POST':
        print('1223')
        login = request.form.get('login')
        password = request.form.get('password')
        password1 = request.form.get('password1')
        print('3333')
        if UsersController.registration(login, password):
            print('1233')
            user = UsersController.show_login(login)
            if password == password1:
                print("1243")
                UsersController.auth(login, password)
                login_user(user)
                return redirect('/vhod')
                # Получаем пользователя
            else:
                message = 'Пароли не совпадают'
        else:
            message = 'Ошибка авторизации после регистрации'
        # else:
        #     message = 'Такой логин уже существует'

    return render_template('registration.html', title=title,message=message)

@application.route('/vhod', methods = ['POST', 'GET'])
@login_required
def vhod():
        title = "Группы студентов"
        if current_user.role_id.id == 1:
            groups = GroupsController.get()



            return render_template('group_students.html',
                                   title=title, groups=groups)
        else:
            return redirect('/logout')

@application.route('/list_students/<int:id>', methods=['POST', 'GET'])
@login_required
def studenti(id):
    title = "Студенты"
    if current_user.role_id.id == 1:
        students = StudentsController.show_group(id)  
        group_name = students[0].group_id.name if students else "Группа не найдена"  # Берём название из первого студента
        return render_template('list_students.html',
                             title=title,
                             students=students,
                             group_name=group_name)
    else:
        return redirect('/logout')


@application.route('/logout')
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    application.run(debug=True)