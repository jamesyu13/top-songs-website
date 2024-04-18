$(document).ready(function() {
    // Combine title and artist and set it as text for #title
    let titleArtist = item.title + " by " + item.artist;
    $("#title").text(titleArtist);

    // Append the edit button to the bottom right corner of the screen
    let editButton = $("<a>").attr("href", "/edit/" + item.id).addClass("edit").html("Edit");
    $("#edit").append(editButton).css({"position": "absolute", "bottom": "20px", "right": "360px"});

    let image = $("<img>").attr("src", item.image).attr("alt", "Album Cover Image").addClass("fixed-image");
    $("#image").append(image);

    // Append the artist name
    $("#artist").append(item.artist);

    $("#link").append(item.link);
    $("#summary").append(item.summary + "<br>"); // Added <br> to create a new line

    // Append the writers
    $("#writers").append(item.writers.join(", ") + "<br>"); // Use join(", ") to add a comma and space between each writer

    $.each(item.genres, function(index, value) {
        let genre = $("<div class='row'></div>").html(value);

        // Add click event to each genre element
        genre.css("cursor", "pointer").on("click", function() {
            // Redirect to search_results page with the clicked genre as the search key
            window.location.href = "/search_results/" + encodeURIComponent(value);
        });

        $("#genres").append(genre);
    });

    // Append peak_pos and weeks_on_chart
    $("#peak_pos").append(item.peak_pos);
    $("#weeks_on_chart").append(item.weeks_on_chart);
});
