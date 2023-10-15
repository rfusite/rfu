$(document).ready(function() {
    $(".show-more-link").on("click", function() {
        var parentDiv = $(this).closest(".text-truncated");
        var shortText = parentDiv.find(".text-short");
        var fullText = parentDiv.find(".text-full");

        if(fullText.is(":hidden")){
            shortText.hide();
            fullText.show();
            $(this).text("less");
        } else {
            fullText.hide();
            shortText.show();
            $(this).text("...more");
        }
    });
});