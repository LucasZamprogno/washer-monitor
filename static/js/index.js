jQuery(function(){
    let loop;
    const check_in_interval = 30000;

    update();
    loop = setInterval(update, check_in_interval);
});

function update() {
    $.get("/status").then((res) => {
        $("span#washer-status").text(res["washer"]["status"]);
        $("span#washer-duration").text(
            minutes_text(res["washer"]["duration"])
        );
        $("span#dryer-status").text(res["dryer"]["status"]);
        $("span#dryer-duration").text(
            minutes_text(res["dryer"]["duration"])
        );
    }).catch((err) => {
        console.log("Update: Connection error (presumably): " + err);
    });
}

function minutes_text(seconds) {
    const minutes = Math.floor(seconds / 60);
    if (minutes === 0) {
        return "less than 1 minute."
    } else if (minutes === 1) {
        return "1 minute."
    } else {
        return minutes + " minutes."
    }
}