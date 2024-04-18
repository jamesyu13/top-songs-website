function error_message(feedback) {
    var template = $("<div class='invalid-feedback'></div>").html(feedback);
    return template;
}

function validate_input(input_s, parent_s, name, error_message, type) {
    var val = $(input_s).val().trim();
    if (val.length == 0 || val.replace(/\s+/g, "").length == 0) {
        $(input_s).addClass("is-invalid");
        $(parent_s).append(error_message);
        return false;
    }

    if (type === "number" && isNaN(Number(val))) {
        $(input_s).addClass("is-invalid");
        $(parent_s).append(error_message);
        return false;
    }

    return true;
}

function validate_inputs() {
    var valid = true;

    valid &= validate_input("#input-title", "#form-title", "title", error_message("Please enter a title."), "");
    valid &= validate_input("#input-artist", "#form-artist", "artist", error_message("Please enter an artist."), "");
    valid &= validate_input("#input-cover", "#form-cover", "cover image URL", error_message("Please enter a cover image URL."), "");
    valid &= validate_input("#input-summary", "#form-summary", "summary", error_message("Please enter a summary."), "");
    valid &= validate_input("#input-weeks", "#form-weeks", "weeks on chart", error_message("Please enter valid weeks on chart."), "number");
    valid &= validate_input("#input-peak", "#form-peak", "peak position", error_message("Please enter a valid peak position."), "number");
    valid &= validate_input("#input-genres", "#form-genres", "genres", error_message("Please enter genres."), "");
    valid &= validate_input("#input-writers", "#form-writers", "writers", error_message("Please enter writers."), "");
    valid &= validate_input("#input-streaming", "#form-streaming", "streaming link", error_message("Please enter a streaming link."), "");

    return valid;
}


$(document).ready(function () {
    $('.alert').hide();

    $("#input-title").val(item["title"])
    $("#input-artist").val(item["artist"])
    $("#input-cover").val(item["image"])
    $("#input-summary").val(item["summary"])
    $("#input-streaming").val(item["link"])
    $("#input-weeks").val(item["weeks_on_chart"])
    $("#input-peak").val(item["peak_pos"])
    $("#input-genres").val(item["genres"])
    $("#input-writers").val(item["writers"])

    $("#new-form").submit(function(event){
        event.preventDefault();

        $(".form-control").removeClass("is-invalid");
        $(".invalid-feedback").remove();
        var valid = validate_inputs();
        if (valid) {
            var new_song = {
                "id": item["id"],
                "title": $("#input-title").val().trim(),
                "artist": $("#input-artist").val().trim(),
                "image": $("#input-cover").val(),
                "summary": $("#input-summary").val().trim(),
                "link": $("#input-streaming").val().trim(),
                "weeks_on_chart": $("#input-weeks").val().trim(),
                "peak_pos": $("#input-peak").val().trim(),
                "genres": $("#input-genres").val().trim(),
                "writers": $("#input-writers").val().trim(),
            };

            $.ajax({
                type: "POST",
                url: "edit_item",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(new_song),
                success: function (response) {
                    console.log("success");
                    let url = response["url"]
                    window.location.href = url
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request);
                    console.log(status);
                    console.log(error);
                }
            });
        }
    });

    $("#discard").click(function(){
        if (confirm("Are you sure you want to discard?") == true){
            window.location.href = "/view/" + item["id"]
        }
    });
});
