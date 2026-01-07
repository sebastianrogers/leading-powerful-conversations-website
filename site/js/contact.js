// Contact form functionality
document.addEventListener("DOMContentLoaded", function () {
  // Show the form only if JavaScript is enabled
  const contactForm = document.getElementById("contact-form");
  if (contactForm) {
    contactForm.style.display = "block";
  }
});

function sendEmail(event) {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const subject = document.getElementById("subject").value;
  const message = document.getElementById("message").value;

  const emailBody = `Name: ${name}%0D%0AEmail: ${email}%0D%0A%0D%0AMessage:%0D%0A${encodeURIComponent(message)}`;
  const mailtoLink = `mailto:sebastian@crazybearandraggedstaff.com?subject=${encodeURIComponent(subject)}&body=${emailBody}`;

  window.location.href = mailtoLink;
}
