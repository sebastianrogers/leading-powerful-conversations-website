// Google Analytics configuration
window.dataLayer = window.dataLayer || [];
function gtag() {
  dataLayer.push(arguments);
}
gtag("js", new Date());
gtag("config", "G-XXXXXXXXXX");

// Mobile navigation toggle functionality
document.addEventListener("DOMContentLoaded", function () {
  const navToggle = document.querySelector(".nav-toggle");
  const navMenu = document.querySelector('nav ul[role="menubar"]');

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", function () {
      const isExpanded = navToggle.getAttribute("aria-expanded") === "true";

      navToggle.setAttribute("aria-expanded", !isExpanded);
      navToggle.classList.toggle("active");
      navMenu.classList.toggle("active");

      // Prevent body scroll when menu is open
      document.body.style.overflow = !isExpanded ? "hidden" : "auto";
    });

    // Close menu when clicking on a link
    const navLinks = navMenu.querySelectorAll("a");
    navLinks.forEach(function (link) {
      link.addEventListener("click", function () {
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.classList.remove("active");
        navMenu.classList.remove("active");
        document.body.style.overflow = "auto";
      });
    });

    // Close menu on escape key
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && navMenu.classList.contains("active")) {
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.classList.remove("active");
        navMenu.classList.remove("active");
        document.body.style.overflow = "auto";
        navToggle.focus();
      }
    });
  }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  });
});

// Parameterized social sharing functions
function shareOnTwitter(customText) {
  const url = encodeURIComponent(window.location.href);
  const text = encodeURIComponent(customText || "Transform your communication skills and lead with impact - Leading Powerful Conversations");
  window.open(`https://twitter.com/intent/tweet?url=${url}&text=${text}&via=leadingconversations`, "_blank", "width=550,height=420");
}

function shareOnFacebook() {
  const url = encodeURIComponent(window.location.href);
  window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, "_blank", "width=550,height=420");
}

function shareOnLinkedIn(customTitle, customSummary) {
  const url = encodeURIComponent(window.location.href);
  const title = encodeURIComponent(customTitle || "Leading Powerful Conversations");
  const summary = encodeURIComponent(
    customSummary ||
      "Transform your communication skills and lead with impact. Discover powerful conversation techniques for Christian leadership, small groups, and spiritual growth."
  );
  window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}&title=${title}&summary=${summary}`, "_blank", "width=550,height=420");
}

function shareViaEmail(customSubject, customBody) {
  const url = window.location.href;
  const subject = encodeURIComponent(customSubject || "Leading Powerful Conversations");
  const body = encodeURIComponent(
    customBody ||
      `I thought you might be interested in this resource for improving communication skills and leadership:\n\n${url}\n\nTransform your communication skills and lead with impact with Leading Powerful Conversations.`
  );
  window.location.href = `mailto:?subject=${subject}&body=${body}`;
}
