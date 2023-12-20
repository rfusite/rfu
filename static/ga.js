// ----------------------------------------------------
// Код для работы с google analytics
// ----------------------------------------------------

// Инициализация dataLayer и gtag
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

// Настройка конфигурации Google Analytics
gtag('config', 'G-EJFM51JQ57');

// Функция для отслеживания кликов на кнопках
function trackButtonEvent(action, category, label) {
    gtag('event', action, {
        'event_category': category,
        'event_label': label
    });
}
