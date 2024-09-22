
    setTimeout(function() {
        const messageContainer = document.getElementById('message-container');
        if (messageContainer) {
            messageContainer.classList.add('fade-out');
            setTimeout(function() {
                messageContainer.style.display = 'none';
            }, 500);  // Allow fade-out time before hiding
        }
    }, 4500);  // Time before starting fade-out
