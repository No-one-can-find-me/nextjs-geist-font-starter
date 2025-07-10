// Minimal JavaScript for essential functionality only
document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide flash messages after 5 seconds (essential for user feedback)
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.display = 'none';
        }, 5000);
    });

    // Simple flash message close button functionality
    const closeButtons = document.querySelectorAll('.flash-close');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.parentElement.style.display = 'none';
        });
    });
});
