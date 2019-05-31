import movies_class
import fresh_tomatoes

avatar = movies_class.Movies("Avatar","Sea voyager to different world","Science fiction","https://cdn.empireonline.com/jpg/80/0/0/1000/563/0/north/0/0/0/0/0/t/films/19995/images/5XPPB44RQGfkBrbJxmtdndKz05n.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8")
robot_2 = movies_class.Movies("Avatar","Sea voyager to different world","Science fiction","","https://www.youtube.com/watch?v=eOrNdBpGMv8")
avengers = movies_class.Movies("Avatar","Sea voyager to different world","Science fiction","","https://www.youtube.com/watch?v=eOrNdBpGMv8")
iron_man = movies_class.Movies("Avatar","Sea voyager to different world","Science fiction","","https://www.youtube.com/watch?v=eOrNdBpGMv8")
de_de_pyar_de = movies_class.Movies("Avatar","Sea voyager to different world","Science fiction","","https://www.youtube.com/watch?v=eOrNdBpGMv8")
andhadhun = movies_class.Movies("Avatar","Sea voyager to different world","Science fiction","","https://www.youtube.com/watch?v=eOrNdBpGMv8")

movies = [avatar,robot_2,avengers,iron_man,de_de_pyar_de,andhadhun]
fresh_tomatoes.open_movies_page(movies)
