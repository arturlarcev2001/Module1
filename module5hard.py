from time import sleep



class User():
    """
    Объект для создания одного пользователя
    nickname - str
    password - hash(str)
    age - int
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video():
    """
    Объект для создания одного видео
    title - str
    duration - int
    time_now - int
    adult_mode - bool
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    
class UrTube():
    """
    Объект для создания основы программы
    users - list
    videos - list
    current_user - str
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    
    def log_in(self, login, password):
        """
        Функция log_in отвечает за вход существующего пользователя
        по средствам ввода логина и пароля
        login - str
        password - hash(str)
        """
        for user in self.users:
            if login == user.nickname and hash(password) == user.password:
                self.current_user = login
            else:
                return 'Проверьте правильность ввода логина и пароля'
    
    def register(self, nickname, password, age):
        """
        Функция для регистрации пользователя на платформе
        nickname - str
        password - hash(str)
        age - int
        """
        user = User(nickname, password, age)
        if len(self.users) == 0:
            self.users.append(user)
            self.current_user = nickname
        else:
            for u in self.users:
                if user.nickname == u.nickname:
                    print("Пользователь {} уже существует".format(nickname))
                    return
                else:
                    self.users.append(user)
                    self.current_user = nickname
                    return        
    
    def log_out(self):
        """
        Функция выхода из сессии
        """
        self.current_user = None
        
    def add(self, *vids):
        """
        Функция для добавления видео на платформу
        vids - list
        """
        for video in vids:
            if video not in self.videos:
                self.videos.append(video)
    
    def get_videos(self, video_name):
        """
        Функция поиска видео на платформе
        video_name - str
        """
        vids = []
        for v in self.videos:
            if video_name.lower() in v.title.lower():
                vids.append(v.title)
        return vids
    
    def watch_video(self, title):
        """
        Функция для поиска видео по его названию и просмотру
        title - str
        """
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if title == video.title and video.adult_mode:
                for user in self.users:
                    if user.nickname == self.current_user:
                        if user.age >= 18:
                            for i in range(video.time_now + 1, video.duration + 1):
                                print(i, end=" ")
                            print("Конец видео")
                            return
                        else:
                            print("Вам нет 18, пожайлуста покиньте страницу")
                            return
                    
    
if __name__ == "__main__":
    ur = UrTube()
    vname1 = "Лучший язык программирования в 2024!"
    vname2 = "Зачем девушке парень программист?"
    v1 = Video(vname1, 200)
    v2 = Video(vname2, 10, adult_mode=True)

    ur.add(v1, v2)

    print(ur.get_videos('зачем'))
    print(ur.get_videos('ПРОГ'))

    ur.watch_video(vname1)
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video(vname2)
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video(vname2)
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

    print(ur.current_user)

    ur.watch_video(vname1)


