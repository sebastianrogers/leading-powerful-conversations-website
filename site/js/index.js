// Affiliate link tracking
function trackAffiliateClick(platform, action, element) {
  // Track with Google Analytics if available
  if (typeof gtag !== "undefined") {
    gtag("event", "affiliate_click", {
      affiliate_platform: platform,
      click_action: action,
      element_id: element,
      value: 1,
      currency: "GBP",
      custom_parameters: {
        source_page: window.location.pathname,
        timestamp: new Date().toISOString(),
      },
    });

    // Track as conversion event
    gtag("event", "conversion", {
      send_to: "G-XXXXXXXXXX/affiliate_click",
      value: 1,
      currency: "GBP",
      transaction_id: "affiliate_" + Date.now(),
    });
  }

  // Track with custom analytics (backup/additional tracking)
  console.log("Affiliate click tracked:", {
    platform: platform,
    action: action,
    element: element,
    url: event.target.href,
    timestamp: new Date().toISOString(),
    page: window.location.href,
  });

  // Optional: Send to your own tracking endpoint
  // This would be useful for detailed affiliate analytics
  /*
  fetch('/api/track-affiliate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      platform: platform,
      action: action,
      element: element,
      url: event.target.href,
      page: window.location.href,
      timestamp: new Date().toISOString(),
      userAgent: navigator.userAgent,
      referrer: document.referrer
    })
  }).catch(err => console.log('Tracking request failed:', err));
  */
}

// Enhanced tracking for all Amazon links
document.addEventListener("DOMContentLoaded", function () {
  // Track all Amazon links on the page
  const amazonLinks = document.querySelectorAll('a[href*="amazon"]');
  amazonLinks.forEach(function (link, index) {
    if (!link.onclick) {
      link.addEventListener("click", function () {
        trackAffiliateClick("amazon", "book_purchase", "amazon_link_" + index);
      });
    }
  });

  // Add hover tracking for engagement analytics
  const affiliateButton = document.getElementById("amazon-affiliate-button");
  if (affiliateButton) {
    let hoverStartTime;

    affiliateButton.addEventListener("mouseenter", function () {
      hoverStartTime = Date.now();
    });

    affiliateButton.addEventListener("mouseleave", function () {
      if (hoverStartTime) {
        const hoverDuration = Date.now() - hoverStartTime;
        if (typeof gtag !== "undefined") {
          gtag("event", "affiliate_hover", {
            duration_ms: hoverDuration,
            element_id: "amazon_button",
          });
        }
      }
    });
  }
});

// Framework carousel navigation
const frameworkPrev = document.querySelector(".framework-prev");
const frameworkNext = document.querySelector(".framework-next");
const frameworkRadios = document.querySelectorAll('input[name="framework"]');

if (frameworkPrev && frameworkNext && frameworkRadios.length > 0) {
  let currentFrameworkSlide = 0;

  function updateFrameworkSlide(direction) {
    if (direction === "next") {
      currentFrameworkSlide = (currentFrameworkSlide + 1) % frameworkRadios.length;
    } else if (direction === "prev") {
      currentFrameworkSlide = (currentFrameworkSlide - 1 + frameworkRadios.length) % frameworkRadios.length;
    }
    frameworkRadios[currentFrameworkSlide].checked = true;
  }

  frameworkNext.addEventListener("click", () => updateFrameworkSlide("next"));
  frameworkPrev.addEventListener("click", () => updateFrameworkSlide("prev"));

  // Update current slide when radio buttons change
  frameworkRadios.forEach((radio, index) => {
    radio.addEventListener("change", () => {
      if (radio.checked) {
        currentFrameworkSlide = index;
      }
    });
  });

  // Auto-advance framework carousel every 8 seconds (optional)
  setInterval(() => {
    updateFrameworkSlide("next");
  }, 8000);
}
