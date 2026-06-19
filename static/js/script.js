// Simple interaction confirmations for engineering validation
document.addEventListener("DOMContentLoaded", function() {
    // Automatically close system notification alerts after 4 seconds
    setTimeout(function() {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 4000);

    // Confirm action before deleting data points
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if(!confirm("Are you sure you want to permanently delete this record?")) {
                e.preventDefault();
            }
        });
    });
});