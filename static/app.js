$(document).ready(function() {
    $(document).on("click", ".show-more-link", function() {
        var parentDiv = $(this).closest(".text-truncated");
        var shortText = parentDiv.find(".text-short");
        var fullText = parentDiv.find(".text-full");
        var moreLink = parentDiv.find(".show-more-link");

        if(fullText.is(":hidden")){
            shortText.hide();
            fullText.show();
            $(this).hide(); // Скрыть "...more" когда текст развернут
        } else {
            fullText.hide();
            shortText.show();
            moreLink.show(); // Показать "...more" когда текст свернут
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll('.like-btn').forEach(function(button) {
    button.addEventListener('click', function(e) {
      const postId = e.currentTarget.getAttribute('data-id');
      fetch(`/api/like/${postId}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
      })
      .then(response => response.json())
      .then(data => {
        document.querySelector(`button[data-id="${postId}"] .like-count`).textContent = ` | ${data.likes}`;
      });
    });
  });
});

function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(function() {
    console.log('Async: Copying to clipboard was successful!');
  }, function(err) {
    console.error('Async: Could not copy text: ', err);
  });
}
