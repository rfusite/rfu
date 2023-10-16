$(document).ready(function() {
    $(document).on("click", ".show-more-link", function() {
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

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
