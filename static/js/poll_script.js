let poll = {
  question: "당신이 좋아하는 아이돌에게 투표하세요!",
  answer: ["MAMAMOO", "TWICE", "BTS", "BLACKPINK"],
  pollCount: 20,
  answersWeight: [3, 3, 5, 9], // sum =20
  selectedAnswer: 0,
};

let pollDOM = {
  question: document.querySelector(".poll .question"),
  answers: document.querySelector(".poll .answers"),
};

pollDOM.question.innerText = poll.question;
pollDOM.answers.innerHTML = poll.answer
  .map(function (answer, i) {
    return `
             <div class="answer" onclick="markAnswer('${i}')">
                ${answer}
                <span class="percentage-bar"></span>
                <span class="percentage-value"></span>
             </div>
            `;
  })
  .join("");

function markAnswer(i) {
  poll.selectedAnswer = +i;
  try {
    document
      .querySelector(".poll .answers .answer .selected")
      .classList.remove("selected");
  } catch (msg) {}
  document
    .querySelectorAll(".poll .answers .answer")
    [+1].classList.add("selected");
  alert("소중한 한 표 감사합니다!");
  showResults();
}

function showResults() {
  let answers = document.querySelectorAll(".poll .answers .answer");
  for (let i = 0; i < answers.length; i++) {
    let percentage = 0;
    if (i == poll.selectedAnswer) {
      percentage = Math.round(
        ((poll.answersWeight[i] + 1) * 100) / (poll.pollCount + 1)
      );
    } else {
      percentage = Math.round(
        (poll.answersWeight[i] * 100) / (poll.pollCount + 1)
      );
    }

    answers[i].querySelector(".percentage-bar").style.width = percentage + "%";
    answers[i].querySelector(".percentage-value").innerText = percentage + "%";
  }
}

const SHOWING_CLASS = "showing";
const firstSlide = document.querySelector(".slider__item:first-child");

function slide() {
  const currentSlide = document.querySelector(`.${SHOWING_CLASS}`);

  if (currentSlide) {
    // 만약 현재 슬라이드라면
    currentSlide.classList.remove(SHOWING_CLASS); // 현재 슬라이드에서 SHOWING_CLASS를 제거한다
    const nextSlide = currentSlide.nextElementSibling; // 다음 슬라이드를 정의한다.

    if (nextSlide) {
      //만약 다음 슬라이드가 있다면
      nextSlide.classList.add(SHOWING_CLASS); //다음 슬라이드에 SHOWING_CLASS를 붙인다.
    } else {
      // 다음 슬라이드가 없다면 =>  5번째 슬라이드라면(마지막 슬라이드라면)
      firstSlide.classList.add(SHOWING_CLASS); // 첫번째 슬라이드에 SHOWING_CLASS를 붙인다.
    }
  } else {
    firstSlide.classList.add(SHOWING_CLASS);
  }
}

slide();
setInterval(slide, 2000);
