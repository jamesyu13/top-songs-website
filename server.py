from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

data = [
   {
       "id": 1,
       "title": "Texas Hold 'Em",
       "artist": "Beyonce",
       "image": "https://charts-static.billboard.com/img/2024/02/beyonce-0na-texasholdem-on7-180x180.jpg",
       "summary": "Texas Hold 'Em is a song by American singer-songwriter Beyoncé from her upcoming eighth studio album, currently under the tentative title Act II. It serves as the album's co-lead single alongside 16 Carriages. The song was a surprise release and debuted during Super Bowl LVIII on February 11, 2024, through Parkwood Entertainment and Columbia Records. Titled after the poker game, Texas Hold 'Em is an uptempo country pop, western and soul song featuring elements of folk music." ,
       "link": "https://open.spotify.com/track/0Z7nGFVCLfixWctgePsRk9?si=c6d58bfcb8d64d3c",
       "weeks_on_chart": "2",
       "peak_pos": "1",
       "genres": ["Country", "Folk", "Pop"],
       "writers": ["Beyoncé", "Brian Bates", "Nate Farraro"]
   },
   {
       "id": 2,
       "title": "Lovin On Me",
       "artist": "Jack Harlow",
       "image": "https://charts-static.billboard.com/img/2023/11/jackharlow-i43-lovinonme-y0w-344x344.jpg",
       "summary": "Lovin on Me is a song by American rapper Jack Harlow. It was released through Generation Now and Atlantic Records as a single on November 10, 2023. Harlow wrote the song with producers Oz, Sean Momberger, and Nik D, alongside Nickie Jon Pabón and Reginald Nelton. The song samples the 1995 R&B track Whatever (Bass Soliloquy) by Cadillac Dale. Prior to its release, a snippet of the song went viral on TikTok. The music video for the song was released the same day.",
       "link": "https://open.spotify.com/track/4xhsWYTOGcal8zt0J161CU?si=6a8796d7880f45f3",
       "weeks_on_chart": "15",
       "peak_pos": "1",
       "genres": ["Rap", "R&B", "Pop"],
       "writers": ["Jack Harlow", "Oz", "Sean Momberger", "Nik D", "Nickie Jon Pabón", "Reginald Nelton"]
   },
   {
       "id": 3,
       "title": "Lose Control",
       "artist": "Teddy Swims",
       "image": "https://charts-static.billboard.com/img/2021/02/teddyswims-vot-344x344.jpg",
       "summary": "Lose Control is a song by American singer-songwriter Teddy Swims, released on June 23, 2023, as the second single from his debut studio album I've Tried Everything but Therapy (Part 1) (2023). Produced by Ammo and Julian Bunetta, it is Swims's first song to reach the Billboard Hot 100, debuting at number 99[1] and peaking at number two. It topped the charts in Belgium and Switzerland.",
       "link": "https://open.spotify.com/track/6usohdchdzW9oML7VC4Uhk?si=b5665022157d4f86",
       "weeks_on_chart": "28",
       "peak_pos": "2",
       "genres": ["Pop", "R&B", "Soul"],
       "writers": ["Teddy Swims", "Ammo", "Julian Bunetta"]
   },
   {
       "id": 4,
       "title": "Carnival",
       "artist": "¥$: Kanye West & Ty Dolla $ign Featuring Rich The Kid & Playboi Carti",
       "image": "https://charts-static.billboard.com/img/2024/02/kanye-west-0wf-carnival-nl0-344x344.jpg",
       "summary": "Carnival is a song by the American superduo ¥$ (composed of rapper Kanye West and singer Ty Dolla Sign) and Rich the Kid, featuring American rapper Playboi Carti. It was released through a single pack on streaming services on February 15 as the third single from the superduo's collaborative album Vultures 1 (2024). The pack also includes Hooligan Version, where only the choir is present, and an a capella version. The digital single cover consists of a still shot from a promo short clip for the album, made by Jon Rafman.",
       "link": "https://open.spotify.com/track/3w0w2T288dec0mgeZZqoNN?si=0abfe493b9364781",
       "weeks_on_chart": "2",
       "peak_pos": "3",
       "genres": ["Trap", "Rage"],
       "writers": ["Kanye West", "Ty Dolla Sign", "Rich the Kid", "Playboi Carti"]
   },
   {
       "id": 5,
       "title": "Beautiful Things",
       "artist": "Benson Boone",
       "image": "https://charts-static.billboard.com/img/2024/02/bensonboone-egp-beautifulthings-vvt-344x344.jpg",
       "summary": "Beautiful Things is a song by American singer and songwriter Benson Boone. It was released on January 18, 2024, through Night Street Records and Warner Records. The song was co-written by Boone with Jack LaFrantz and Evan Blair, and produced by the latter. It reached number one in Austria, Canada, the Czech Republic, Norway and Switzerland.",
       "link": "https://open.spotify.com/track/6tNQ70jh4OwmPGpYy6R2o9?si=9570e1dff9714e56",
       "weeks_on_chart": "5",
       "peak_pos": "3",
       "genres": ["Folk Rock", "Pop"],
       "writers": ["Benson Boone", "Jack LaFrantz", "Evan Blair"]
   },
   {
       "id": 6,
       "title": "Snooze",
       "artist": "SZA",
       "image": "https://charts-static.billboard.com/img/2022/12/sza-xyh-snooze-eom-344x344.jpg",
       "summary": "Snooze is a song by American singer-songwriter SZA from her second studio album, SOS (2022). It was sent to rhythmic contemporary and urban contemporary radio as the sixth single from the album on April 25, 2023. SZA wrote the song with producers Babyface, the Rascals (Leon Thomas III and Khristopher Riddick-Tynes), and BLK. The acoustic version features Canadian singer Justin Bieber, who stars in the official music video of the song's original version, and was released on September 15, 2023.",
       "link": "https://open.spotify.com/track/4iZ4pt7kvcaH6Yo8UoZ4s2?si=d3d75cfcc8f94bb8",
       "weeks_on_chart": "62",
       "peak_pos": "2",
       "genres": ["R&B"],
       "writers": ["SZA", "Babyface", "Leon Thomas III", "Khristopher Riddick-Tynes", "BLK"]
   },
   {
       "id": 7,
       "title": "Cruel Summer",
       "artist": "Taylor Swift",
       "image": "https://charts-static.billboard.com/img/2019/08/taylor-swift-9sy-cruelsummer-i1p-344x344.jpg",
       "summary": "Cruel Summer is a song by the American singer-songwriter Taylor Swift from her seventh studio album, Lover (2019). The song was written by Swift, Jack Antonoff, and St. Vincent, and was produced by Swift and Antonoff. Cruel Summer is a synth-pop, industrial pop, and electropop song composed of synths, wobbling beats, and vocoder-manipulated vocals. The lyrics are about an intense romance during a painful summer.",
       "link": "https://open.spotify.com/track/1BxfuPKGuaTgP7aM0Bbdwr?si=f4997adcc27b446d",
       "weeks_on_chart": "42",
       "peak_pos": "1",
       "genres": ["Synth-pop", "Industrial-pop"],
       "writers": ["Taylor Swift", "Jack Antonoff", "St. Vincent"]
   },
   {
       "id": 8,
       "title": "Greedy",
       "artist": "Tate McRae",
       "image": "https://charts-static.billboard.com/img/2023/09/tatemcrae-rxu-greedy-2h2-344x344.jpg",
       "summary": "Greedy is a song by Canadian singer and dancer Tate McRae. It was released through RCA Records on September 15, 2023, as the lead single of her second studio album Think Later (2023). The song was written by McRae, alongside Amy Allen, Jasper Harris, and OneRepublic lead singer Ryan Tedder; production was handled by the latter two along with Grant Boutin. Lyrically, McRae described the song as an ode to female empowerment. Greedy was commercially successful, peaking at number one on the Billboard Global 200 and Canadian Hot 100.",
       "link": "https://open.spotify.com/track/3rUGC1vUpkDG9CZFHMur1t?si=252931e41ccf4224",
       "weeks_on_chart": "23",
       "peak_pos": "3",
       "genres": ["Dance-pop", "Pop", "R&B"],
       "writers": ["Tate McRae", "Amy Allen", "Jasper Harris", "Ryan Tedder"]
   },
   {
       "id": 9,
       "title": "I Remember Everything",
       "artist": "Zach Bryan Featuring Kacey Musgraves",
       "image": "https://charts-static.billboard.com/img/2023/09/zachbryan-de1-iremembereverything-to3-344x344.jpg",
       "summary": "I Remember Everything is a song by American singer Zach Bryan featuring country music artist Kacey Musgraves. It appeared as track eleven on his fourth studio album Zach Bryan, released on August 25, 2023, and was sent to radio airplay in Italy on September 8, as the lead single from the album. The song debuted at number one on the US Billboard Hot 100, becoming both Bryan's and Musgraves's first number-one song.",
       "link": "https://open.spotify.com/track/4KULAymBBJcPRpk1yO4dOG?si=786be3e941ae4d53",
       "weeks_on_chart": "26",
       "peak_pos": "1",
       "genres": ["Country"],
       "writers": ["Zach Bryan", "Kacey Musgraves"]
   },
   {
       "id": 10,
       "title": "Agora Hills",
       "artist": "Doja Cat",
       "image": "https://charts-static.billboard.com/img/2018/04/dojacat-cqv-344x344.jpg",
       "summary": "Agora Hills is a song by American rapper and singer Doja Cat from her fourth studio album, Scarlet (2023). It was released on October 3, 2023, through Kemosabe and RCA Records as the second single from the album. A pop-infused slow jam with a trap beat, it finds Doja Cat discussing the ways in which she wants to flaunt her partner, despite the pressures of fame and secrecy. Directed by Hannah Lux Davis, the accompanying music video is 1990s-inspired and sees her traversing an apocalyptic California landscape with her supernatural female friends.",
       "link": "https://open.spotify.com/track/7dJYggqjKo71KI9sLzqCs8?si=cf910993697948fb",
       "weeks_on_chart": "22",
       "peak_pos": "7",
       "genres": ["Pop", "Hip-hop"],
       "writers": ["Doja Cat"]
   }
]

current_id = 12
names = []
for d in data:
    names.append(d["title"])

@app.route('/')
def main():
    return render_template('home.html', data=data, names=names)


@app.route('/search_results/<searchkey>', methods=['GET', 'POST'])
def search(searchkey):
    global data
    res = []

    for d in data:
        # Join genres and capitalize each genre
        genres_string = ", ".join(map(str.capitalize, d["genres"]))

        if searchkey in d["title"].lower():
            # Highlight search word in title
            d["matched"] = "title"
            d["start"] = d["title"].lower().find(searchkey)
            d["end"] = d["start"] + len(searchkey)
            res.append(d)
        elif searchkey in d["summary"].lower():
            # Highlight search word in summary
            d["matched"] = "summary"
            pos = d["summary"].lower().find(searchkey.lower())
            if pos != -1:
                i = max(0, d["summary"][:pos].rfind(".") + 1)
                j = min(len(d["summary"]), pos + d["summary"][pos:].find(".") + len(searchkey))
                d["extra"] = d["summary"][i:j]
                d["start"] = max(0, d["extra"].lower().find(searchkey.lower()))
                d["end"] = d["start"] + len(searchkey)
                res.append(d)
        elif searchkey.lower() in d["artist"].lower():
            # Highlight search word in artist
            d["matched"] = "artist"
            d["start"] = d["artist"].lower().find(searchkey.lower())
            d["end"] = d["start"] + len(searchkey)
            res.append(d)
        elif searchkey.lower() in genres_string.lower():
            # Highlight search word in genres
            d["matched"] = "genres"
            d["start"] = genres_string.lower().find(searchkey.lower())
            d["end"] = d["start"] + len(searchkey)
            d["extra"] = genres_string
            res.append(d)

    return render_template('search_results.html', results=res, searchkey=searchkey, names=names)



@app.route('/view/<id>')
def view(id=0):
    global data
    id = int(id)
    for d in data:
        if d["id"] == id:
            return render_template('view.html', names=names, item=d)
    return render_template('view.html', names=names, item=d)


@app.route('/add')
def add():
    return render_template("add.html", names=names)


@app.route('/add_item', methods=['POST'])
def add_item():
    global data
    global current_id
    new_item = request.get_json()
    current_id += 1
    new_item["id"] = current_id

    # Split writers by comma and strip spaces from each writer
    if "writers" in new_item:
        writers_str = new_item["writers"]
        new_item["writers"] = [writer.strip() for writer in writers_str.split(",")]

    # Split genres by comma and strip spaces from each genre
    if "genres" in new_item:
        genres_str = new_item["genres"]
        new_item["genres"] = [genre.strip() for genre in genres_str.split(",")]

    data.append(new_item)
    return jsonify(url="view/" + str(new_item["id"]))



@app.route('/edit/<id>')
def edit(id):
    global data
    for item in data:
        if item["id"] == int(id):
            return render_template('edit.html', names=names, item=item)
    else:
        print("id not valid")


@app.route('/edit/edit_item', methods=['GET', 'POST'])
def edit_item():
    global data
    item_updated = request.get_json()
    # Split genres and writers by commas and remove leading/trailing whitespaces
    if "genres" in item_updated:
        item_updated["genres"] = [x.strip() for x in item_updated["genres"].split(",")]
    if "writers" in item_updated:
        item_updated["writers"] = [x.strip() for x in item_updated["writers"].split(",")]
    for i, item in enumerate(data):
        if item["id"] == item_updated["id"]:
            data[i] = item_updated
    return jsonify(url="/view/" + str(item_updated["id"]))



if __name__ == '__main__':
    app.run(debug=True)
