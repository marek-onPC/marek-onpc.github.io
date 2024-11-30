<script lang="ts">
  import type { CheatSheetCardType } from '../types';

  export let cheatSheetData: CheatSheetCardType;
</script>

<div class="card">
  <h4>{cheatSheetData.title}</h4>
  <p>{cheatSheetData.is_published ? 'Published' : 'Draft'}</p>
  <div>
    {#if cheatSheetData.categories}
      <p>Categories:</p>
      {#each cheatSheetData.categories as category}
        <p>{category}</p>
      {/each}
    {/if}
  </div>
</div>
