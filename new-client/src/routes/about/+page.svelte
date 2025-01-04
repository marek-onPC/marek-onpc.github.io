<div class="about">
  <p>
    <span class="highlight">Hello! I'm Marek</span>, a Software Engineer with more than four years
    of professional experience, based in Japan.
  </p>
  <p>
    I am currently working as a <span style="color: #42b883; font-weight: 400"
      >Lead Software Engineer</span
    >.
  </p>
  <p>
    I specialize in both front-end and back-end development, and I'm also active in the data and
    DevOps fields. Always eager to learn new technologies, I also enjoy coding for fun after work.
  </p>
  <div class="about__border"></div>
  <p>
    <span class="highlight">This page</span> serves as my playground for learning and testing different
    technologies.
  </p>
  <p>It has been rewritten a couple of times over the past few years.</p>
  <p>
    Currently, it’s built with <span style="color: #EC4D29; font-weight: 400">Svelte</span>
    (front-end), <span style="color: #4B8BBE; font-weight: 400">Python</span> with the FastAPI
    framework (back-end), and <span style="color: #4DB33B; font-weight: 400">MongoDB</span> as the
    database.<br /> Additionally, it's containerized with
    <span style="color: #0DB7ED; font-weight: 400">Docker</span>, tested with
    <span style="color: #FFE873; font-weight: 400">pytest</span>, and deployed with
    <span style="color: #C9C3E6; font-weight: 400">Heroku</span>.
  </p>
  <p style="margin-top: 50px;"><span class="highlight">Previously built with:</span></p>
  <ul class="about__timeline">
    <li class="about__timeline-item">
      <span style="color: #00749C; font-weight: 400">WordPress</span> (theme from scratch) +
      <span style="color: #F29111; font-weight: 400">MySQL</span>
    </li>
    <li class="about__timeline-item">
      <span style="color: #42b883; font-weight: 400">Vue</span> +
      <span style="color: #00749C; font-weight: 400">WordPress</span>
      (RestAPI) + <span style="color: #F29111; font-weight: 400">MySQL</span>
    </li>
    <li class="about__timeline-item">
      <span style="color: #61DBFB; font-weight: 400">React</span> +
      <span style="color: #00749C; font-weight: 400">WordPress</span>
      (RestAPI) + <span style="color: #F29111; font-weight: 400">MySQL</span>
    </li>
    <li class="about__timeline-item">
      <span style="color: #61DBFB; font-weight: 400">React</span> +
      <span style="color: #4B8BBE; font-weight: 400">Python</span>
      + <span style="color: #4DB33B; font-weight: 400">MongoDB</span>
    </li>
  </ul>
</div>

<style lang="scss">
  .about {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 1200px;
    margin: 50px;

    p {
      font-size: 20px;
      font-weight: 300;
      color: #fff;
      margin-bottom: 10px;
      text-align: center;

      .highlight {
        font-size: 30px;
        color: #42b883;
      }
    }

    &__border {
      display: block;
      height: 1px;
      width: 80%;
      margin: 40px 0px 20px 0px;
      border-bottom: 1px solid #42b883;
    }

    &__timeline {
      display: flex;
      flex-direction: column-reverse;
      list-style: none;
      counter-reset: list-number;
      padding: 0px;
      margin-left: 35px;
      position: relative;

      &::after {
        content: '';
        height: 150px;
        width: 2px;
        background-color: #42b883;
        position: absolute;
        top: 15px;
        left: 12.5px;
      }

      &-item {
        counter-increment: list-number;
        font-size: 20px;
        font-weight: 300;
        color: #fff;
        margin-bottom: 25px;
        z-index: 100;

        &:before {
          content: counter(list-number);
          display: inline-block;
          font-size: 18px;
          font-weight: 300;
          line-height: 24px;
          height: 26px;
          width: 26px;
          text-align: center;
          margin-right: 45px;
          background-color: #42b883;
          border-radius: 50%;
        }
      }
    }
  }
</style>
