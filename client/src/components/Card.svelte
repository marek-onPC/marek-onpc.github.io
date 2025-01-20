<script lang="ts">
  import { onMount } from 'svelte';
  import type { CheatSheetCardType } from '../types';

  export let cheatSheetData: CheatSheetCardType;
  export let showShowStatus: boolean = false;

  let title: string;

  onMount(() => {
    title = cheatSheetData.title;

    if (title.length > 25) {
      title = title.slice(0, 25);
      title += '...';
    }
  });
</script>

<div class="card" title={cheatSheetData.title !== title ? cheatSheetData.title : ''}>
  <h4 class="card__title">{title}</h4>
  {#if showShowStatus}
    <p class="card__publish">{cheatSheetData.is_published ? 'Published' : 'Draft'}</p>
  {/if}
  <div class="card__lang">
    <p class="card__lang-heading">Language:</p>
    <p class="card__lang-type">{cheatSheetData.language ? cheatSheetData.language : 'None'}</p>
  </div>
</div>

<style lang="scss">
  .card {
    width: auto;
    max-width: 300px;
    background-color: #fff;
    padding: 15px;
    margin: 0 10px 20px 10px;
    border-radius: 5px;
    border: 2px solid #fff;
    transition: 0.25s ease-in-out;
    position: relative;
    cursor: pointer;

    &:hover {
      border: 2px solid #42b883;

      .card__title {
        color: #42b883;
      }

      .card__publish {
        opacity: 0;
      }
    }

    &__title {
      font-weight: 600;
      font-size: 20px;
      margin-top: 0;
      margin-bottom: 10px;
      padding-bottom: 5px;
      border-bottom: 1px solid #42b883;
      transition: 0.25s ease-in-out;
    }

    &__publish {
      font-size: 14px;
      margin-top: 0;
      text-align: right;
      opacity: 0.75;
      position: absolute;
      right: 15px;
      bottom: 0px;
      transition: 0.25s ease-in-out;
    }

    &__lang {
      display: flex;
      font-size: 14px;
      opacity: 0.85;
      min-height: 50px;

      &-heading {
        margin-top: 0;
        margin-bottom: 5px;
        margin-right: 10px;
      }

      &-type {
        margin-top: 0;
        margin-bottom: 5px;
      }
    }
  }
</style>
