<script lang="ts">
  import { goto } from '$app/navigation';
  import { fetchClientPost } from '$lib/fetchClient';
  import { sessionToken } from '../../../stores';

  let isLoading: boolean = false;
  let isError: boolean = false;

  const createNewCheatSheet = async () => {
    try {
      isLoading = true;
      isError = false;

      const newCheatSheetID = await fetchClientPost('/cheat_sheets', $sessionToken, {
        title: 'test',
        is_published: false
      });
      goto(`/dashboard/cheat-sheet/${newCheatSheetID.id}`);
    } catch (error) {
      isLoading = false;
      isError = true;
    }
    isLoading = false;
  };
</script>

<div class="new-cheat-sheet">
  <button
    class={`button new-cheat-sheet__submit ${isLoading ? '--disabled' : ''}`}
    on:click={createNewCheatSheet}
    disabled={isLoading}
  >
    {isLoading ? '...' : 'CREATE NEW'}
  </button>

  {#if isError}
    <div class="new-cheat-sheet__error">
      <p>Error occurred on creating new cheat sheet, try again.</p>
    </div>
  {:else}
    <div class="new-cheat-sheet__spacer"></div>
  {/if}
</div>

<style lang="scss">
  .new-cheat-sheet {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: 100%;
    margin-top: 100px;

    &__submit {
      height: 50px;
      width: 200px;

      &.--disabled {
        background-color: #2e805b;
      }
    }

    &__error {
      border-radius: 5px;
      margin-top: 50px;
      padding: 0px 20px;
      background-color: rgb(253, 237, 237);

      p {
        color: rgb(95, 33, 32);
        font-size: 14px;
      }
    }

    &__spacer {
      display: block;
      background-color: transparent;
      height: 96.5px;
    }
  }
</style>
