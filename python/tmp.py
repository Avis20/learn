genres = [
    {
      "_index": "genres",
      "_id": "0b105f87-e0a5-45dc-8ce7-f8632088f390",
      "_source": {
        "id": "0b105f87-e0a5-45dc-8ce7-f8632088f390",
        "name": "Western"
      }
    },
    {
      "_index": "genres",
      "_id": "120a21cf-9097-479e-904a-13dd7198c1dd",
      "_source": {
        "id": "120a21cf-9097-479e-904a-13dd7198c1dd",
        "name": "Adventure"
      }
    },
]

films = [
    {
        "_index": "movies",
        "_id": "8d4f3766-a857-49a3-ae9c-4565a9459a29",
        "_source": {
            "id": "8d4f3766-a857-49a3-ae9c-4565a9459a29",
            "imdb_rating": 6.9,
            "title": "Man Without a Star",
            "description": "Dempsey Rae, a cowboy with no clear aim in life, winds up working on a spread with a hard lady owner just arrived from the East. She needs a tough new top hand and uses all her means of persuasion to get Rae to take the job. But he doesn't like the way the other settlers are getting treated and starts to side with them, despite their introduction of the barbed wire he loathes.",
            "genre": [
                "Western"
            ]
        }
    }
]

def random_films_by_genre():
    result = []
    for genre in genres:
        item = {"genre": genre, "films": []}
        for film in films:
            film_genres = film['_source']['genre']
            if genre['_source']['name'] in film_genres:
                item["films"].append(film)
        result.append(item)
    return result

if __name__ == '__main__':
    print(random_films_by_genre())

