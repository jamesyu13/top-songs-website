$(document).ready(function(){
    $("#searchresults").empty();
    
    let toprow = $("<div>").addClass("row toprow").html("Search Results for '" + searchkey + "'");
    $("#searchresults").append(toprow);

    let resultCountMessage = results.length === 0 ? "No results found" : results.length + " results found";
    let numresults = $("<div>").addClass("row result").html(resultCountMessage);
    $("#searchresults").append(numresults);

    $.each(results, function(index, item){
        let result = $("<div>").addClass("row eachresult");
        let title = $("<a>").attr("href", "/view/" + item["id"]).addClass("titlesearch");
        let st = item["start"];
        let en = item["end"];

        if (item["matched"] === "title") {
            let name = item["title"];
            title.html(name);
            result.append(title);
            result.append("<br>");
            result.append(item["title"].slice(0, st) + "<span class='highlight-result border-secondary'>" + item["title"].slice(st, en) + "</span>" + item["title"].slice(en));
        } else if (item["matched"] === "artist") { // Check if matched item is artist
            title.html(item["title"]);
            result.append(title);
            result.append("<br>");
            result.append(item["artist"].slice(0, st) + "<span class='highlight-result border-secondary'>" + item["artist"].slice(st, en) + "</span>" + item["artist"].slice(en));
        } else {
            title.html(item["title"]);
            result.append(title);
            result.append("<br>");
            result.append(item["extra"].slice(0, st) + "<span class='highlight-result border-secondary'>" + item["extra"].slice(st, en) + "</span>" + item["extra"].slice(en));
        }

        result.append("<br>");
        $("#searchresults").append(result);
    });
});
