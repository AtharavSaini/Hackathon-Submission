window.onload = () => {

  /* ============ FETCH BACKEND DATA ============ */

  const data = JSON.parse(localStorage.getItem("education_result"));

  if (!data || !data.insights) {
    alert("No education loan data found");
    window.location.href = "index.html";
    return;
  }

  const score = Number(
    data.approval_percentage ?? data.raw_score ?? 0
  );

  const summary =
    data.insights.summary || "Education loan profile";

  const insightsData =
    data.insights.insights || [];

  /* ============ SCORE + LABEL ============ */

  document.getElementById("currentScore").innerText = score;
  document.getElementById("currentScoreSmall").innerText = score;

  const label = document.getElementById("profileLabel");
  label.innerText = summary;

  if (score < 50) {
    label.style.background = "rgba(255,95,95,0.15)";
    label.style.color = "#ff5f5f";
  } else if (score < 75) {
    label.style.background = "rgba(255,183,3,0.15)";
    label.style.color = "#ffb703";
  } else {
    label.style.background = "rgba(77,213,153,0.15)";
    label.style.color = "#4dd599";
  }

  /* ============ INSIGHTS RENDER ============ */

  const container = document.getElementById("insightContainer");
  container.innerHTML = "";

  if (!insightsData || insightsData.length === 0) {
    container.innerHTML = `
      <div class="insight-card info">
        <h3>No major risks detected</h3>
        <p class="impact">
          Your education loan profile looks strong.
        </p>
        <p class="solution">
          Maintain academic consistency and financial discipline.
        </p>
      </div>
    `;
  } else {
    insightsData.forEach(item => {

      let riskClass = "info";
      const issue = item.issue.toLowerCase();

      if (
        issue.includes("very high") ||
        issue.includes("below") ||
        issue.includes("no ")
      ) {
        riskClass = "danger";
      } else if (
        issue.includes("high") ||
        issue.includes("moderate")
      ) {
        riskClass = "warning";
      }

      container.innerHTML += `
        <div class="insight-card ${riskClass}">
          <h3>${item.issue}</h3>
          <p class="impact">
            Impact: ${item.impact}
          </p>
          <p class="solution">
            Improvement: ${item.improvement}
          </p>
        </div>
      `;
    });
  }

  /* ============ EXPECTED IMPROVEMENT ============ */

  let improvementText = "+5 to +10";

  if (score < 40) improvementText = "+25 to +35";
  else if (score < 60) improvementText = "+15 to +25";

  document.getElementById("potentialScore").innerText =
    improvementText;

  /* ============ ACTION BUTTONS ============ */

  document.getElementById("recalculateBtn").onclick = () => {
    window.location.href = "education.html";
  };

  document.getElementById("exploreLoansBtn").onclick = () => {
    window.location.href = "result_education.html";
  };

};
