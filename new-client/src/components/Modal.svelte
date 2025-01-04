<script lang="ts">
  import { onDestroy, onMount } from 'svelte';
  import Loader from './Loader.svelte';

  export let isOpened: boolean;
  export let text: string;
  export let hasLoader: boolean = false;
  export let callback: () => void = () => {};

  onMount(() => (document.body.style.overflow = 'hidden'));
  onDestroy(() => (document.body.style.overflow = ''));
</script>

<div class="modal">
  <div class="modal__background"></div>
  <div class="modal__window">
    <p class="modal__text">{text}</p>
    <div class="modal__footer">
      {#if hasLoader}
        <Loader smallMargin={true} />
      {:else}
        <button class="button modal__button" on:click={callback}>Delete</button>
        <button class="button modal__button --cancel" on:click={() => (isOpened = false)}
          >Cancel
        </button>
      {/if}
    </div>
  </div>
</div>

<style lang="scss">
  .modal {
    position: absolute;
    top: -5px;
    left: -5px;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;

    &__background {
      content: '';
      position: absolute;
      top: -5px;
      left: -5px;
      width: 100vw;
      height: 100vh;
      background-color: rgba(0, 0, 0, 0.5);
      z-index: 1;
    }

    &__window {
      width: auto;
      height: auto;
      z-index: 2;
      background-color: #fff;
      padding: 25px;
      border-radius: 5px;

      @media screen and (max-width: 500px) {
        top: 0px;
        left: 0px;
        width: 100vw;
        height: 100vh;
        padding-top: 150px;
      }
    }

    &__text {
      text-align: center;
      font-weight: 600;
      margin-bottom: 50px;
    }

    &__footer {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
    }

    &__button {
      margin: 5px;

      &.--cancel {
        background-color: orange;

        &:hover {
          background-color: rgb(189, 123, 0);
        }
      }
    }
  }
</style>
