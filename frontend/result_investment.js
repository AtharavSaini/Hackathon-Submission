window.onload = () => {

  const data = JSON.parse(localStorage.getItem("investment_result"));

  if (!data) {
    alert("No investment result found");
    window.location.href = "index.html";
    return;
  }

  /* ================= SCORE ================= */

  const rawScore = Number(
    data.score ?? data.approval_percentage ?? data.raw_score ?? 0
  );

  const score = isNaN(rawScore) ? 0 : Math.max(0, Math.min(100, rawScore));

  document.querySelector(".score-value").innerText = score;

  /* ================= NEEDLE ROTATION ================= */

  const angle = -90 + (score * 180) / 100;
  const needle = document.querySelector(".meter-needle");

  if (needle) {
    needle.style.transform = `translateX(-50%) rotate(${angle}deg)`;
  }

  /* ================= LABEL COLOR ================= */

  const labels = document.querySelectorAll(".score-labels span");
  labels.forEach(l => l.classList.remove("active"));

  if (score < 40) labels[0].classList.add("active");
  else if (score < 60) labels[1].classList.add("active");
  else if (score < 80) labels[2].classList.add("active");
  else labels[3].classList.add("active");

  /* ================= INVESTMENT CARDS ================= */

  const section = document.querySelector(".loan-section");
  section.innerHTML = "<h2>Investment Opportunities</h2>";

  const schemes =
    data.recommended_schemes?.schemes ||
    data.recommended_schemes ||
    [];

  // 🔥 LOW SCORE / NO SCHEME FIX
  if (!schemes || schemes.length === 0) {
    section.innerHTML += `
      <div class="no-loans">
        <h3>No investment options available</h3>
        <p style="opacity:0.7">
          Improve traction, revenue or team strength to unlock investor interest.
        </p>
      </div>
    `;
  } else {
    schemes.forEach((inv, i) => {
      section.innerHTML += `
        <div class="loan-card ${i === 0 ? "highlight" : ""}">
          <div class="loan-left">
            <h3>${inv.provider || inv.name || "Investor"}</h3>
            <p class="meta">
              <span>${inv.stage || ""}</span>
              <span>${inv.amount || ""}</span>
              <span>${inv.type || ""}</span>
            </p>
            <p class="tag">${inv.ui_label || ""}</p>
          </div>
          ${
            inv.link
              ? `<a href="${inv.link}" target="_blank" class="details">
                   View Details →
                 </a>`
              : ""
          }
        </div>
      `;
    });
  }

  /* ================= FIND MORE OPTIONS ================= */

  const findMoreBtn = document.querySelector(".actions .secondary");

  if (findMoreBtn) {
    findMoreBtn.onclick = () => {
      window.location.href = "index.html";
    };
  }

  /* ================= IMPROVE SCORE ================= */

  const boostBtn = document.querySelector(".actions .primary");

  if (boostBtn) {
    boostBtn.onclick = () => {
      window.location.href = "boost_investment.html";
    };
  }

};
