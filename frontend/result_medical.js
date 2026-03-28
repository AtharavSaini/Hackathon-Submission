window.onload = () => {

  const data = JSON.parse(localStorage.getItem("medical_result"));

  if (!data) {
    alert("No medical result found");
    window.location.href = "index.html";
    return;
  }

  /* ================= SCORE ================= */

  const rawScore = Number(
    data.approval_percentage ?? data.raw_score ?? 0
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

  /* ================= LOAN CARDS ================= */

  const section = document.querySelector(".loan-section");
  section.innerHTML = "<h2>Loan Opportunities</h2>";

  const schemes =
    data.recommended_schemes?.schemes ||
    data.recommended_schemes ||
    [];

  // 🔥 LOW SCORE / NO SCHEME FIX
  if (!schemes || schemes.length === 0) {
    section.innerHTML += `
      <div class="no-loans">
        <h3>No loans available for this score</h3>
        <p style="opacity:0.7">
          Improve income, credit score or reduce EMIs to unlock loan options.
        </p>
      </div>
    `;
  } else {
    schemes.forEach((loan, i) => {
      section.innerHTML += `
        <div class="loan-card ${i === 0 ? "highlight" : ""}">
          <div class="loan-left">
            <h3>${loan.provider}</h3>
            <p class="meta">
              <span>${loan.interest_rate}</span>
              <span>${loan.amount}</span>
              <span>${loan.tenure}</span>
            </p>
            <p class="tag">${loan.ui_label || ""}</p>
          </div>
          <a href="${loan.link}" target="_blank" class="details">
            View Details →
          </a>
        </div>
      `;
    });
  }

  /* ================= FIND MORE LOANS (ALWAYS WORK) ================= */

  const findMoreBtn = document.querySelector(".actions .secondary");

  if (findMoreBtn) {
    findMoreBtn.onclick = () => {
      window.location.href = "step1.html";
    };
  }

  /* ================= BOOST MY SCORE ================= */

const boostBtn = document.querySelector(".actions .primary");

if (boostBtn) {
  boostBtn.onclick = () => {
    window.location.href = "boost_medical.html";
  };
}


};













