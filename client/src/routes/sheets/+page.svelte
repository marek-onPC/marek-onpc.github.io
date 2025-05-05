<script lang="ts">
  import { fetchClientGetWithoutToken } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import type { CheatSheetWithContentType } from '../../types';
  import Card from '../../components/Card.svelte';
  import Loader from '../../components/Loader.svelte';

  let cheatSheetsData: Array<CheatSheetWithContentType>;

  const loadCheatSheets = async () => {
    try {
      const raw = await fetchClientGetWithoutToken('/cheat_sheets');
      cheatSheetsData = raw.data as Array<CheatSheetWithContentType>;
    } catch (e) {
      console.log(e);
    }
  };

  onMount(() => {
    loadCheatSheets();
  });
</script>

<p class="sheets__description">
  There’s no strict rule for what ends up here — it’s just a <span class="highlight"
    >mix of code snippets</span
  > I’ve found handy over time. Some are super simple, others a bit more complex. A few came from real-world
  projects, while others are just results from studying or experimenting. I put them here for easy access,
  to quickly access them when needed.
</p>
<div class="sheets__list">
  {#if cheatSheetsData}
    {#each cheatSheetsData as card}
      <a href={`/sheets/${card.id}`}><Card cheatSheetData={card} /></a>
    {/each}
  {:else}
    <Loader />
  {/if}
</div>

<style lang="scss">
  .sheets {
    &__description {
      font-size: 18px;
      font-weight: 300;
      color: #fff;
      margin-bottom: 10px;
      text-align: center;
      margin-bottom: 35px;

      .highlight {
        font-size: 24px;
        color: #42b883;
      }
    }

    &__list {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      align-content: flex-start;

      a {
        text-decoration: inherit;
        color: inherit;
        cursor: auto;
        width: 100%;
        max-width: 300px;
      }
    }
  }
</style>
