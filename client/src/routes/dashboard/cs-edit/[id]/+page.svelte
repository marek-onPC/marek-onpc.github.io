<script lang="ts">
  import { page } from '$app/stores';
  import { fetchClientDelete, fetchClientGet, fetchClientPatch } from '$lib/fetchClient';
  import { onMount } from 'svelte';
  import { sessionToken } from '../../../../stores';
  import type { CheatSheetWithContentType } from '../../../../types.js';
  import Loader from '../../../../components/Loader.svelte';
  import Modal from '../../../../components/Modal.svelte';
  import { goto } from '$app/navigation';
  import Checkbox from '../../../../components/Checkbox.svelte';
  import { switchPlaces } from '$lib/arrays';
  import { flip } from 'svelte/animate';

  const cheatSheetId = $page.params.id;
  let isOpenedDeleteModal: boolean = false;
  let isDeleted: boolean = false;
  let initCheatSheetData: CheatSheetWithContentType;
  let updatedCheatSheetData: CheatSheetWithContentType;

  const loadCheatSheet = async () => {
    try {
      const cheetSheet = await fetchClientGet(`/cheat_sheets/${cheatSheetId}`, $sessionToken.token);
      initCheatSheetData = cheetSheet.data as CheatSheetWithContentType;
      updatedCheatSheetData = structuredClone(initCheatSheetData);
    } catch (e) {
      console.log(e);
    }
  };

  const updateCheatSheet = async () => {
    try {
      await fetchClientPatch(`/cheat_sheets/${cheatSheetId}`, $sessionToken.token, {
        title: updatedCheatSheetData.title,
        language: updatedCheatSheetData.language,
        is_published: updatedCheatSheetData.is_published,
        cards: updatedCheatSheetData.cards
      });
      initCheatSheetData = structuredClone(updatedCheatSheetData);
    } catch (e) {
      console.log(e);
    }
  };

  const deleteCheatSheet = async () => {
    try {
      await fetchClientDelete(`/cheat_sheets/${cheatSheetId}`, $sessionToken.token);
      isDeleted = true;
      isOpenedDeleteModal = false;
      goto('/dashboard');
    } catch (e) {
      console.log(e);
    }
  };

  const addCheatSheetCard = async () => {
    !updatedCheatSheetData.cards
      ? (updatedCheatSheetData.cards = [{ subtitle: '', content: '' }])
      : (updatedCheatSheetData.cards = [
          ...updatedCheatSheetData.cards,
          { subtitle: '', content: '' }
        ]);
  };

  const removeCheatSheetCard = async (indexToRemove: number) => {
    if (updatedCheatSheetData.cards) {
      const afterRemoval = updatedCheatSheetData.cards.filter((_, index) => {
        return index !== indexToRemove;
      });

      updatedCheatSheetData.cards = [...afterRemoval];

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
  {#if isOpenedDeleteModal}
    <Modal
      bind:isOpened={isOpenedDeleteModal}
      text={`Would you like to delete ${updatedCheatSheetData.title} cheat sheet?`}
      callback={deleteCheatSheet}
    />
  {/if}
  {#if initCheatSheetData && !isDeleted}
    <div class="update__header">
      <div class="update__title-wrapper">
        <input
          name="title"
          type="text"
          class="update__title"
          bind:value={updatedCheatSheetData.title}
        />
        <label for="title">title</label>
      </div>
      <div class="update__language-wrapper">
        <input
          name="language"
          type="text"
          class="update__language"
          bind:value={updatedCheatSheetData.language}
        />
        <label for="language">language</label>
      </div>
      <Checkbox title="Publish" bind:isChecked={updatedCheatSheetData.is_published} />
      <button class="button update__delete" on:click={() => (isOpenedDeleteModal = true)}>♻</button
      >
    </div>
    {#if updatedCheatSheetData.cards}
      {#each updatedCheatSheetData.cards as card, index (card)}
        <div class="update__edit-card-wrapper" animate:flip={{ duration: 250 }}>
          <input
            class="update__edit-card-title"
            name={`${updatedCheatSheetData.id}_${index}_title`}
            id={`${updatedCheatSheetData.id}_${index}_title`}
            bind:value={card.subtitle}
          />
          <label for={`${updatedCheatSheetData.id}_${index}_title`}>subtitle</label>
          <button class="update__remove-card" on:click={() => removeCheatSheetCard(index)}
            >♻</button
          >
          <div class="update__edit-card-divider"></div>
          <textarea
            class="update__edit-card-content"
            name={`${updatedCheatSheetData.id}_${index}`}
            id={`${updatedCheatSheetData.id}_${index}`}
            bind:value={card.content}
          />
          <label class="update__edit-card-label" for={`${updatedCheatSheetData.id}_${index}`}
            >cheat-sheet content</label
          >
          {#if updatedCheatSheetData.cards}
            {#if index > 0}
              <button
                class="update__move-up-card arrow-up"
                on:click={() =>
                  (updatedCheatSheetData.cards = switchPlaces(
                    updatedCheatSheetData.cards || [],
                    index,
                    index - 1
                  ))}>▲</button
              >
            {/if}

            {#if index < updatedCheatSheetData.cards.length - 1}
              <button
                class="update__move-down-card"
                on:click={() =>
                  (updatedCheatSheetData.cards = switchPlaces(
                    updatedCheatSheetData.cards || [],
                    index,
                    index + 1
                  ))}>▼</button
              >
            {/if}
          {/if}
        </div>
      {/each}
    {/if}

    <button class="button update__add" on:click={addCheatSheetCard}>+</button>
    {#if JSON.stringify(initCheatSheetData) !== JSON.stringify(updatedCheatSheetData)}
      <button class="button update__save" on:click={updateCheatSheet}>Save</button>
    {/if}
  {:else}
    <Loader />
  {/if}
</div>

<style lang="scss">
  .update {
    &__page {
      display: flex;
      flex-direction: column;
      width: auto;
    }

    &__header {
      display: flex;
      width: auto;
    }

    &__title,
    &__language {
      width: 100%;
      font-size: 18px;
      font-weight: 600;
      text-align: center;
      padding: 25px 10px 10px 10px;
      margin: 0px 10px 35px 0px;
      border: none;
      border-radius: 5px;
      border: 2px solid #fff;
      transition: 0.25s ease-in-out;

      &:focus {
        outline: none;
        border: 2px solid #42b883;
      }
    }

    &__language {
      margin: 0px 10px 35px 10px;
      width: 100px !important;
    }

    &__title-wrapper {
      width: 100% !important;
    }

    &__delete {
      color: #fff;
      background-color: rgb(165, 2, 2);
      height: 60px !important;
      width: 65px;
      font-weight: 800;
      font-size: 40px;
      line-height: 22px;
      transition: 0.25s ease-in-out;
      cursor: pointer;
      border-width: 0px;
      border-radius: 5px;
      margin-left: 15px;
      padding-top: 3px;

      &:hover {
        background-color: rgb(107, 9, 9);
      }
    }

    &__edit-card-title {
      font-weight: 600;
      text-align: center;
      padding: 25px 35px 10px 35px;
      border-radius: 5px;
      border: 2px solid #fff;
      transition: 0.25s ease-in-out;
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
    }

    &__edit-card-divider {
      height: 32px;
      background-color: #fff;
      transition: 0.25s ease-in-out;
      border: 2px solid #fff;
      border-bottom: none;
      margin: -1px 0px -1px 0px;
    }

    &__edit-card-content {
      min-height: 75px;
      padding: 10px;
      border-radius: 5px;
      border: 2px solid #fff;
      border-top: #fff;
      transition: 0.25s ease-in-out;
      margin: 0 0 5px 0;
      scrollbar-width: thin;
      border-top-left-radius: 0;
      border-top-right-radius: 0;
      font-family: 'Courier New', monospace;
      font-weight: 600;
    }

    &__edit-card-label {
      top: 60px !important;
      left: 7.5px !important;
    }

    &__remove-card {
      position: absolute;
      top: 0;
      left: 0;
      color: #fff;
      background-color: rgb(165, 2, 2);
      height: 32px !important;
      width: 24px;
      font-size: 24px;
      font-weight: 800;
      line-height: 22px;
      padding: 0px 0px 5px 0;
      border-top-left-radius: 5px;
      border-bottom-right-radius: 5px;
      transition: 0.25s ease-in-out;
      cursor: pointer;
      border-width: 0px;
    }

    &__move-up-card,
    &__move-down-card {
      position: absolute;
      top: 0;
      right: 0;
      color: #fff;
      background-color: #42b883;
      height: 23px !important;
      width: 23px;
      font-weight: 800;
      line-height: 22px;
      padding: 0px 5px;
      transition: 0.25s ease-in-out;
      cursor: pointer;
      border-width: 0px;
    }

    &__move-up-card {
      &.arrow-up {
        border-top-right-radius: 5px;
      }
    }

    &__move-down-card {
      top: 28px;
    }

    &__title-wrapper,
    &__edit-card-wrapper,
    &__language-wrapper {
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

    &__language-wrapper {
      label {
        left: 17.5px;
      }

      &:focus-within {
        label {
          left: 15px;
        }
      }
    }

    &__edit-card-wrapper {
      flex-direction: column;

      label {
        top: 5px;
        left: 29px;
      }

      &:focus-within {
        label {
          top: 3.5px;
          left: 23px;
        }

        .update__edit-card-label {
          top: 50px !important;
          left: 5px !important;
        }

        .update__remove-card {
          top: 2px;
          left: 2px;
          height: 16px !important;
          width: 18px;
          font-weight: 800;
          line-height: 16px;
          font-size: 12px;
          border-top-left-radius: 3px;
          border-bottom-right-radius: 3px;
        }

        .update__edit-card-content,
        .update__edit-card-title {
          padding: 20px 35px 10px 10px;
          outline: none;
          border: 2px solid #42b883;
        }

        .update__edit-card-title {
          border-bottom: 1px solid #42b883;
        }

        .update__edit-card-divider {
          height: 20px;
          border: 2px solid #42b883;
          border-top: 2px solid #42b883;
          border-bottom: none;
        }

        .update__edit-card-content {
          padding: 10px 10px 10px;
          min-height: 300px;
          border-top: none;
        }

        .update__move-down-card {
          top: 23px;
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
