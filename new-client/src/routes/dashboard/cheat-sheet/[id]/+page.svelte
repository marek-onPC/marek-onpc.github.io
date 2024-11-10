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
      updatedCheatSheetData = {
        ...initCheatSheetData,
        content: initCheatSheetData.content ? [...initCheatSheetData.content] : undefined
      };
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
      initCheatSheetData = {
        ...updatedCheatSheetData,
        content: updatedCheatSheetData.content ? [...updatedCheatSheetData.content] : undefined
      };
    } catch (e) {
      console.log(e);
    }
  };

  const addCheatSheetCard = async () => {
    console.log(updatedCheatSheetData.content);
    !updatedCheatSheetData.content
      ? (updatedCheatSheetData.content = [''])
      : (updatedCheatSheetData.content = [...updatedCheatSheetData.content, '']);
  };

  const removeCheatSheetCard = async (indexToRemove: number) => {
    console.log(indexToRemove);
    if (updatedCheatSheetData.content) {
      const afterRemoval = updatedCheatSheetData.content.filter((_, index) => {
        return index !== indexToRemove;
      });

      updatedCheatSheetData.content = [...afterRemoval];

      const focusedElement = document.activeElement as HTMLElement | null;
      if (focusedElement) {
        focusedElement.blur();
      }
    }
  };

  onMount(() => {
    loadCheatSheet();
  });
</script>

<div class="update__page">
  {#if initCheatSheetData}
    <div class="update__title-wrapper">
      <input
        name="title"
        type="text"
        class="update__title"
        bind:value={updatedCheatSheetData.title}
        on:keydown={() => {
          console.log(initCheatSheetData, updatedCheatSheetData);
        }}
      />
      <label for="title">title</label>
    </div>
    {#if updatedCheatSheetData.content}
      {#each updatedCheatSheetData.content as card, index}
        <div class="update__edit-card-wrapper">
          <textarea
            class="update__edit-card"
            name={`${updatedCheatSheetData.id}_${index}`}
            id={`${updatedCheatSheetData.id}_${index}`}
            bind:value={card}
          />
          <label for={`${updatedCheatSheetData.id}_${index}`}>cheat-sheet</label>
          <button class="update__remove-card" on:click={() => removeCheatSheetCard(index)}
            >🗑</button
          >
        </div>
      {/each}
    {/if}

    <button class="button update__add" on:click={addCheatSheetCard}>+</button>
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
      width: 100%;
      font-size: 18px;
      font-weight: 600;
      text-align: center;
      padding: 25px 10px 10px 10px;
      margin-bottom: 35px;
      border: none;
      border-radius: 5px;
      border: 2px solid #fff;
      transition: 0.25s ease-in-out;

      &:focus {
        padding: 15px 10px 10px 10px;
        outline: none;
        border: 2px solid #42b883;
      }
    }

    &__edit-card {
      width: 100%;
      min-height: 25px;
      padding: 30px 10px 10px 10px;
      border: none;
      border-radius: 5px;
      border: 2px solid #fff;
      transition: 0.25s ease-in-out;
      margin: 5px 0;
      scrollbar-width: thin;

      &:focus {
        padding: 20px 10px 10px 10px;
        min-height: 200px;
        outline: none;
        border: 2px solid #42b883;
      }
    }

    &__remove-card {
      position: absolute;
      top: 5px;
      left: 0;
      color: #fff;
      background-color: rgb(165, 2, 2);
      height: 24px !important;
      width: 20px;
      font-weight: 800;
      line-height: 22px;
      padding: 0px 5px;
      border-top-left-radius: 5px;
      border-bottom-right-radius: 5px;
      transition: 0.25s ease-in-out;
      cursor: pointer;
      border-width: 0px;
    }

    &__title-wrapper,
    &__edit-card-wrapper {
      display: flex;
      width: auto;
      position: relative;

      label {
        position: absolute;
        top: 2.5px;
        left: 7.5px;
        font-size: 16px;
        color: #35495e;
        transition: 0.25s ease-in-out;
        opacity: 0.5;
      }

      &:focus-within {
        label {
          top: 0px;
          left: 5px;
          font-size: 12px;
          color: #42b883;
          opacity: 1;
        }
      }
    }

    &__edit-card-wrapper {
      label {
        top: 7.5px;
        left: 25px;
      }

      &:focus-within {
        label {
          top: 5px;
          left: 22.5px;
        }

        .update__remove-card {
          top: 7px;
          left: 2px;
          height: 16px !important;
          width: 18px;
          font-weight: 800;
          line-height: 16px;
          font-size: 12px;
          border-top-left-radius: 3px;
          border-bottom-right-radius: 3px;
        }
      }
    }

    &__add {
      width: 50px;
      margin: 25px auto;
    }

    &__save {
      margin: 25px auto;
    }
  }
</style>
