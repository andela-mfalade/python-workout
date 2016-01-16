import fresh_tomatoes
import media


feel_alive = media.Movie(
    "Feel Alive",
    "Some random inspirational rock song I found on Facebook",
    "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRnkFrXPZxRjNrLPdPQTv35f_m9_XjTiN8Ui9Dtu5TtBEWGmiICeQ",
    "https://www.youtube.com/watch?v=2iMKnzFDCL4"
)

mortal_kombat = media.Movie(
    "Mortal Kombat",
    "My favorite old time game",
    "http://images.vcpost.com/data/images/full/38368/mortal-kombat-x.jpg",
    "https://www.youtube.com/watch?v=jSi2LDkyKmI"
)

call_of_duty = media.Movie(
    "Call Of Duty",
    "One of my fav gunplay games",
    "http://pre01.deviantart.net/9ca0/th/pre/f/2013/134/3/7/cod_ghosts_poster_by_realrobdesign-d65b33j.png",
    "https://www.youtube.com/watch?v=7P-xrAphYn4"
)

hit_man = media.Movie(
    "Hit Man",
    "I used to love this game too.",
    "http://static.srcdn.com/slir/w786-h1164-q90-c786:1164/wp-content/uploads/hitman-agent-47-poster.jpg",
    "https://www.youtube.com/watch?v=GadR4G3Hhd4"
)

lions_king = media.Movie(
    "Lion's King",
    "One of the best animations ever produced",
    "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRwUCe2SfAmmyRZOpTc9iJI5oR2SSUaeNTSP0_Z13sWQwqPfD7jnQ",
    "https://www.youtube.com/watch?v=GaJWzJfoXlE"
)

wolverine_vs_the_hulk = media.Movie(
    "Wolvering VS The Hulk",
    "Not seen this so I don't know the story line and I'm damn too lazy to search for it.",
    "http://img15.deviantart.net/22be/i/2012/040/4/4/hulk_vs_wolverine_by_gonzzo-d4p6zie.jpg",
    "https://www.youtube.com/watch?v=EjejVuwSqgI"
)

gods_of_egypt = media.Movie(
    "Gods of Egypt",
    "Not seen this so I don't know the story line and I'm damn too lazy to search for it.",
    "http://filmystuff.com/wp-content/uploads/2015/11/God-of-Egypt-Teaser-Poster-review-images-cast-wiki.jpg",
    "https://www.youtube.com/watch?v=IJBnK2wNQSo"
)

x_men_apocalypse = media.Movie(
    "X-Men Apocalypse",
    "Not seen this so I don't know the story line and I'm damn too lazy to search for it.",
    "http://41.media.tumblr.com/922209da0f3d47b08f180630a9962f6c/tumblr_nr8q39lS1k1ux1imeo1_1280.jpg",
    "https://www.youtube.com/watch?v=N0io2w_6vT8"
)

black_road = media.Movie(
    "Black Road",
    "Not seen this so I don't know the story line and I'm damn too lazy to search for it.",
    "http://cdn.traileraddict.com/content/unknown/black-road.jpg",
    "https://www.youtube.com/watch?v=lcEc2-hd4Zw"
)

daddy_is_home = media.Movie(
    "Daddy's Home",
    "Not seen this so I don't know the story line and I'm damn too lazy to search for it.",
    "http://image.tmdb.org/t/p//original/jzyYHkLGGsF8lSdDfrQOnpXnk8j.jpg",
    "https://www.youtube.com/watch?v=mgNs89c_DLY"
)



movies = [
    daddy_is_home,
    call_of_duty,
    black_road,
    gods_of_egypt,
    x_men_apocalypse,
    hit_man,
    feel_alive,
    mortal_kombat,
    lions_king,
    wolverine_vs_the_hulk
]
fresh_tomatoes.open_movies_page(movies)
