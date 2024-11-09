<script lang="ts">
  import { page } from '$app/stores';
  import { fetchClientGet, fetchClientPatch } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import { sessionToken } from '../../../../stores';
  import type { CheatSheetWithContentType } from '../../../../types.js';

  const cheatSheetId = $page.params.id;
  let initCheatSheetData: CheatSheetWithContentType;
  let updatedCheatSheetData: CheatSheetWithContentType;

  const loadCheatSheet = async () => {
    try {
      const cheetSheet = await fetchClientGet(`/cheat_sheets/${cheatSheetId}`, $sessionToken);
      initCheatSheetData = JSON.parse(cheetSheet.data) as CheatSheetWithContentType;
      updatedCheatSheetData = { ...initCheatSheetData };
    } catch (e) {
      console.log(e);
    }
  };

  const updateCheatSheet = async () => {
    try {
      await fetchClientPatch(`/cheat_sheets/${cheatSheetId}`, $sessionToken, {
        title: updatedCheatSheetData.title,
        categories: updatedCheatSheetData.categories,
        is_published: updatedCheatSheetData.is_published,
        content: updatedCheatSheetData.content
      });
      initCheatSheetData = { ...updatedCheatSheetData };
    } catch (e) {
      console.log(e);
    }
  };

  onMount(() => {
    loadCheatSheet();
  });
</script>

<div class="update__page">
  {#if initCheatSheetData}
    <input
      type="text"
      class="update__title"
      bind:value={updatedCheatSheetData.title}
      on:keydown={() => {
        console.log(initCheatSheetData, updatedCheatSheetData);
      }}
    />
    {#if JSON.stringify(initCheatSheetData) !== JSON.stringify(updatedCheatSheetData)}
      <button class="button update__save" on:click={updateCheatSheet}>Save</button>
    {/if}
  {:else}
    <p>Loading</p>
  {/if}
</div>

<style lang="scss">
  .update {
    &__page {
      display: flex;
      flex-direction: column;
      width: auto;
      margin-top: 50px;
    }

    &__title {
      font-size: 18px;
      font-weight: 600;
      text-align: center;
      padding: 10px;
      border: none;
      border-radius: 5px;
      border: 2px solid #fff;
      transition: 0.25s ease-in-out;

      &:focus {
        outline: none;
        border: 2px solid #42b883;
      }
    }

    &__save {
      margin: 25px auto;
    }
  }
</style>
