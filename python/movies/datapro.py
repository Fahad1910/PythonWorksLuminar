from json import load
path="C:\\Users\\Asus\\Desktop\\Luminar\\movies\\mdb.json"
with open(path,encoding="utf-8") as f:
    filims=load(f)

# print total number of filims
# print(len(filims))

# print all movie names released in 2015
movie_filter=[f.get("title") for f in filims if f.get("year")=="2015"]
# print(movie_filter)

# print comedy genre movie title
funny_movies=[f.get("title") for f in filims if "Comedy" in f.get("genres")]
# print(funny_movies)

# id in range (20,30) and runtime > 110
mfilter=[f.get("title") for f in filims if f.get("id") in range(20,31) and f.get("runtime")>="110"]
# print(mfilter)

# print one word title movie director or title
title_filter=[f.get("title") for f in filims if len(f.get("title").split(" "))==1]
# print(title_filter)

# genre=drama highest runtime
drama_movies=[f for f in filims if "Drama" in f.get("genres")]
lengthy_movie=max(drama_movies,key=lambda f:int(f.get("runtime")))
# print(lengthy_movie)


# print all genres
# []

# q2) in which year more movie released

wc={}
for m in filims:
    year=m.get("year")

    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1

# out=max(wc,key=lambda y:wc.get(y))
# print(out)#,wc.get(out)

# print(max((v,k) for k,v in wc.items()))



# shop={"samsung":10,"apple":20,"redmi":145,"oppo":45}

# out=max([(v,k) for k,v in shop.items()])

# print(out)