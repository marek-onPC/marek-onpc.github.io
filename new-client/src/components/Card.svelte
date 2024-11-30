<script lang="ts">
  import { onMount } from 'svelte';
  import type { CheatSheetCardType } from '../types';

  export let cheatSheetData: CheatSheetCardType;

  let title: string;

  onMount(() => {
    title = cheatSheetData.title;

    if (title.length > 14) {
      title = title.slice(0, 14);
      title += '...';
    }
  });
</script>

<div class="card" title={cheatSheetData.title !== title ? cheatSheetData.title : ''}>
  <h4 class="card__title">{title}</h4>
  <p class="card__publish">{cheatSheetData.is_published ? 'Published' : 'Draft'}</p>
  <div class="card__categories">
    <p class="card__categories-heading">Categories:</p>
    {#if cheatSheetData.categories}
      {#each cheatSheetData.categories as category}
        <p class="card__categories-category">{category}</p>
      {/each}
    {:else}
      <p class="card__categories-category">None</p>
    {/if}
  </div>
</div>

<style lang="scss">
  .card {
    width: 200px;
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
      top: 12px;
      transition: 0.25s ease-in-out;
    }

    &__categories {
      display: flex;
      font-size: 14px;
      opacity: 0.85;
      min-height: 50px;

      &-heading {
        margin-top: 0;
        margin-bottom: 5px;
        margin-right: 10px;
      }

      &-category {
        margin-top: 0;
        margin-bottom: 5px;
      }
    }
  }
</style>
