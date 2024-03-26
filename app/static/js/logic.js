$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});


// call Flask API endpoint
function makePredictions() {
    var fixed_acidity = $("#fixed_acidity").val();
    var volatile_acidity = $("#volatile_acidity").val();
    var citric_acid = $("#citric_acid").val();
    var residual_sugar = $("#residual_sugar").val();
    var chlorides = $("#chlorides").val();
    var free_sulfur_dioxide = $("#free_sulfur_dioxide").val();
    var total_sulfur_dioxide = $("#total_sulfur_dioxide").val();
    var density = $("#density").val();
    var pH = $("#pH").val();
    var sulphates = $("#sulphates").val();
    var alcohol = $("#alcohol").val();

    console.log("step 1 completed")

    // check if inputs are valid

    // create the payload
    var payload = {
        "fixed_acidity": fixed_acidity,
        "volatile_acidity": volatile_acidity,
        "citric_acid": citric_acid,
        "residual_sugar": residual_sugar,
        "chlorides": chlorides,
        "free_sulfur_dioxide": free_sulfur_dioxide,
        "total_sulfur_dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol
    }

    console.log("step 2 completed")

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            let prediction = returnedData["prediction"]

            if (prediction["wine_pred"] === "red") {
                $("#output").text("Go try some red wines!");
            } else {
                $("#output").text("Have you thought about trying white wines?");
            }

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}