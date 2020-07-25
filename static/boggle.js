$("#submit-word").on("submit", handleSubmit)

// handles submitting the users word. If the word is not valid, fires an alert. Else, adds 
// the word to the html list.
async function handleSubmit(event) {
    event.preventDefault();
    $chosenInputWord = $("#chosen-word").val()

    let response = await axios.post("/api/score-word", json={"word": $chosenInputWord});
    
    if (response.data.result === "not-word" || response.data.result === "not-on-board") {
        alert("This is not a legal play!");
    } else {
        let $newLi = $("<li>");
        $newLi.text($chosenInputWord);
        $("#words").append($newLi);
    }
}


// I can technically make the result="ok" the if conditional and all others fail
// as the else statement for brevity