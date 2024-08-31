<script lang="ts">
  import {
    faJs,
    faReact,
    faPython,
    faVuejs,
    faSass,
    faPhp
  } from '@fortawesome/free-brands-svg-icons';
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import { fade } from 'svelte/transition';

  import type { IconSet } from '../types';
  import { onMount } from 'svelte';

  const ICONS: ReadonlyArray<IconSet> = [
    {
      icon: faJs,
      color: '#F0DB4F'
    },
    {
      icon: faReact,
      color: '#61DBFB'
    },
    {
      icon: faVuejs,
      color: '#42B883'
    },
    {
      icon: faPython,
      color: '#4B8BBE'
    },
    {
      icon: faPhp,
      color: '#B0B3D6'
    },
    {
      icon: faSass,
      color: '#CC6699'
    }
  ];

  let mounted = false;

  onMount(() => {
    mounted = true;
  });
</script>

<div class="home">
  <div class="background">
    <div class="circle circle__xxlarge"></div>
    <div class="circle circle__xlarge"></div>
    <div class="circle circle__large"></div>
    <div class="circle circle__medium"></div>
    <div class="circle circle__small"></div>
  </div>

  <div class="content">
    {#if mounted}
      <div class="content__left">
        <h1 transition:fade={{ delay: 500 }} class="content__name">Marek Śmieja</h1>
        <h2 transition:fade={{ delay: 750 }} class="content__title">software engineer</h2>
        <div transition:fade={{ delay: 1000 }} class="content__border"></div>
        {#each ICONS as icon, index}
          <div
            transition:fade|global={{ delay: 1250 + index * 150 }}
            style="display: inline-block; padding-right: 10px; color: {icon.color}"
          >
            <FontAwesomeIcon icon={icon.icon} color={icon.color} pull="left" size="3x" />
          </div>
        {/each}
      </div>
      <div transition:fade={{ delay: 750 }} class="content__right">
        <a href="/about" class="button">ABOUT</a>
      </div>
    {/if}
  </div>
</div>

<style lang="scss">
  .home {
    width: 100%;
  }

  .circle {
    position: absolute;
    border-radius: 50%;
    background: #42b883;
    animation: ripple 15s infinite;

    &__small {
      width: 20vw;
      height: 20vw;
      right: calc(-10vw - 1px);
      bottom: calc(-10vw - 1px);
      opacity: 0.9;
    }

    &__medium {
      width: 30vw;
      height: 30vw;
      right: calc(-15vw - 1px);
      bottom: calc(-15vw - 1px);
      opacity: 0.7;
    }

    &__large {
      width: 40vw;
      height: 40vw;
      right: calc(-20vw - 1px);
      bottom: calc(-20vw - 1px);
      opacity: 0.6;
    }

    &__xlarge {
      width: 50vw;
      height: 50vw;
      right: calc(-25vw - 1px);
      bottom: calc(-25vw - 1px);
      opacity: 0.4;
    }

    &__xxlarge {
      width: 60vw;
      height: 60vw;
      right: calc(-30vw - 1px);
      bottom: calc(-30vw - 1px);
      opacity: 0.2;
    }
  }

  .content {
    display: flex;
    flex-direction: column;
    padding: 80px 30px;
    overflow: hidden;

    @media (min-width: 600px) {
      flex-direction: row;
      padding: 80px 50px;
    }

    &__left {
      width: 100%;

      @media (min-width: 600px) {
        width: 60%;
      }
    }

    &__right {
      display: flex;
      justify-content: center;
      width: 100%;
      margin: auto;
      margin-top: 50px;

      @media (min-width: 600px) {
        width: 40%;
        margin-top: auto;
      }
    }

    &__name {
      font-size: 3.5rem;
      line-height: 1.167;
      font-weight: 100;
      color: #42b883;
      margin: 0px;

      @media (min-width: 600px) {
        font-size: 4.7rem;
      }

      @media (min-width: 900px) {
        font-size: 5.25rem;
      }

      @media (min-width: 1200px) {
        font-size: 6rem;
      }
    }

    &__title {
      font-size: 2rem;
      line-height: 1.167;
      font-weight: 200;
      color: #42b883;
      margin: 0px;

      @media (min-width: 600px) {
        font-size: 2.5rem;
      }

      @media (min-width: 900px) {
        font-size: 2.75rem;
      }

      @media (min-width: 1200px) {
        font-size: 3rem;
      }
    }

    &__border {
      width: 100%;
      max-width: 415px;
      height: 1px;
      margin-top: 60px;
      margin-bottom: 25px;
      background-color: #42b883;
    }
  }

  @keyframes ripple {
    0% {
      transform: scale(0.8);
    }

    50% {
      transform: scale(1.2);
    }

    100% {
      transform: scale(0.8);
    }
  }
</style>
