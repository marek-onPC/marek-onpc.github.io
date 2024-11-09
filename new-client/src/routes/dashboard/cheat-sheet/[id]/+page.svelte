<script lang="ts">
  import { page } from '$app/stores';
  import { fetchClientGet } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import { sessionToken } from '../../../../stores';
  import type { CheatSheetWithContentType } from '../../../../types.js';

  const cheatSheetId = $page.params.id;
  let cheatSheetData: CheatSheetWithContentType;

  const loadCheatSheet = async () => {
    try {
      const cheetSheet = await fetchClientGet(`/cheat_sheets/${cheatSheetId}`, $sessionToken);
      cheatSheetData = JSON.parse(cheetSheet.data) as CheatSheetWithContentType;
    } catch (e) {
      console.log(e);
    }
  };

  onMount(() => {
    loadCheatSheet();
  });
</script>

{#if cheatSheetData}
  <p>{cheatSheetData.id}</p>
{:else}
  <p>Loading</p>
{/if}
