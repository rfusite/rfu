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

function copyToClipboard(textToCopy, buttonElement) {
  navigator.clipboard.writeText(textToCopy).then(function() {
    console.log('Async: Copying to clipboard was successful!');

    // Инициализируем tooltip
    var tooltip = new bootstrap.Tooltip(buttonElement, {
      title: "Текст скопирован в буфер обмена!"
    });
    tooltip.show();

    // Удаляем tooltip и снимаем фокус с кнопки после того, как он показался
    setTimeout(function() {
      tooltip.dispose(); // Удаляем tooltip
      buttonElement.blur(); // Снимаем фокус с кнопки
    }, 1500); // Время отображения tooltip в миллисекундах
  }, function(err) {
    console.error('Async: Could not copy text: ', err);
  });
}

// ----------------------------------------------------
// Код для работы с cookie согласия
// ----------------------------------------------------

document.addEventListener('DOMContentLoaded', function() {
    if (getCookie('user_cookie_consent') !== 'accepted') {
        document.getElementById('cookieConsentContainer').style.display = 'block';
    }

    document.getElementById('acceptCookies').onclick = function() {
        setCookie('user_cookie_consent', 'accepted', 365); // Устанавливаем cookie на 1 год
        document.getElementById('cookieConsentContainer').style.display = 'none';
    };

    document.getElementById('declineCookies').onclick = function() {
        setCookie('user_cookie_consent', 'declined', 365); // Устанавливаем cookie на 1 год
        document.getElementById('cookieConsentContainer').style.display = 'none';
    };
});

function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
