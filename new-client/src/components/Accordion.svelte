<script lang="ts">
  import { fade } from 'svelte/transition';

  export let title: string;

  let isCollapsed: boolean = true;
</script>

<div class="accordion">
  <button
    class={`accordion__title ${isCollapsed ? '--collapsed' : ''}`}
    on:click={() => (isCollapsed = !isCollapsed)}>{title}</button
  >
  {#if !isCollapsed}
    <div
      class="accordion__content"
      in:fade={{ duration: 250, delay: 125 }}
      out:fade={{ duration: 125 }}
    >
      <slot />
    </div>
  {/if}
</div>

<style lang="scss">
  .accordion {
    width: 100%;
    margin: 25px 15px;

    @media screen and (max-width: 800px) {
      max-width: 600px;
    }

    @media screen and (max-width: 1200px) {
      max-width: 800px;
    }

    &__title {
      display: block;
      width: 100%;
      height: auto !important;
      cursor: pointer;
      font-size: 2.75rem;
      font-weight: 200;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
        'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
      text-align: left;
      color: #42b883;
      outline: none;
      background-color: transparent;
      border: none;
      border-bottom: 2px solid #42b883;
      padding: 10px;
      position: relative;

      &::after {
        position: absolute;
        top: calc(50% - 24px);
        right: 6px;
        display: block;
        content: 'collapse';
        font-size: 16px;
        width: 20px;
        height: 20px;
        line-height: 19px;
        -webkit-font-smoothing: antialiased;
        transform: rotateZ(90deg);
        transform-origin: 10px;
        transition: all 0.25s ease-in-out;

        @media screen and (max-width: 400px) {
          font-size: 12px;
          top: auto;
          bottom: 30px;
          right: -5px;
        }
      }

      &.--collapsed::after {
        transform: rotateZ(0deg);
        top: calc(50% - 10px);
        right: 38px;
        content: 'expand';

        @media screen and (max-width: 400px) {
          font-size: 12px;
          top: auto;
          bottom: 0px;
          right: 17px;
        }
      }
    }

    &__content {
      margin-top: 50px;
      padding-left: 50px;
      border-left: 2px solid #42b883;
      position: relative;

      @media screen and (max-width: 800px) {
        margin-top: 25px;
        padding-left: 25px;
      }

      @media screen and (max-width: 600px) {
        margin-top: 15px;
        padding-left: 15px;
      }

      &::after {
        position: absolute;
        top: -50px;
        left: -2px;
        display: block;
        content: '';
        width: 2px;
        height: 50px;
        background-color: #42b883;

        @media screen and (max-width: 800px) {
          top: -25px;
          height: 25px;
        }

        @media screen and (max-width: 600px) {
          top: -16px;
          height: 16px;
        }
      }
    }
  }
</style>
