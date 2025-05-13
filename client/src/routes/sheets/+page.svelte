<script lang="ts">
  import { fetchClientGet, fetchClientGetWithoutToken } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import type { CheatSheetWithContentType } from '../../types';
  import Card from '../../components/Card.svelte';
  import Loader from '../../components/Loader.svelte';
  import { slide } from 'svelte/transition';
  import { sessionToken } from '../../stores';

  let cheatSheetsData: Array<CheatSheetWithContentType>;
  let isLongLoading = false;

  const loadCheatSheets = async () => {
    try {
      const raw = await fetchClientGetWithoutToken('/cheat_sheets');
      cheatSheetsData = raw.data as Array<CheatSheetWithContentType>;
      isLongLoading = false;
    } catch (e) {
      console.log(e);
    }
  };

  const loadAllCheatSheets = async () => {
    try {
      const raw = await fetchClientGet('/cheat_sheets', $sessionToken.token, {
        is_published__list: [true, false]
      });
      cheatSheetsData = raw.data as Array<CheatSheetWithContentType>;
      isLongLoading = false;
    } catch (e) {
      console.log(e);
    }
  };

  const checkLoading = () => {
    if (cheatSheetsData) {
      isLongLoading = false;
    } else {
      isLongLoading = true;
    }
  };

  onMount(() => {
    if (!$sessionToken.token || $sessionToken.expiry < new Date()) {
      loadCheatSheets();
    } else {
      loadAllCheatSheets();
    }
    setTimeout(() => {
      checkLoading();
    }, 3000);
  });
</script>

<p class="sheets__description">
  There’s no strict rule for what ends up here — it’s just a <span class="highlight"
    >mix of code snippets</span
  > I’ve found handy over time. Some are super simple, others a bit more complex. A few came from real-world
  projects, while others are just results from studying or experimenting. I put them here for easy access
  when needed.
</p>

{#if isLongLoading}
  <div class="sheets__notif" transition:slide={{ duration: 250 }}>
    <p>⚡ Waking up the server... this might take a few seconds...</p>
  </div>
{/if}

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

    &__notif {
      display: flex;
      justify-content: center;
      align-items: center;
      width: calc(100% - 40px);
      max-width: 500px;
      margin: 0 auto;
      padding: 20px;
      background-color: #42b883;
      color: #fff;
      font-size: 18px;
      font-weight: 400;
      border-radius: 5px;
      position: absolute;
      bottom: 25px;
      left: 10px;

      p {
        margin: 0;
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
