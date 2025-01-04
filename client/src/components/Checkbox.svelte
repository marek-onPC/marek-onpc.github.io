<script lang="ts">
  export let isChecked: boolean;
  export let title: string;
</script>

<label class="checkbox">
  <p>{title}</p>
  <input type="checkbox" bind:checked={isChecked} />
  <span class="checkmark"></span>
</label>

<style lang="scss">
  :global(.checkbox) {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 7.5px;
    cursor: pointer;
    width: 60px;
    height: 45px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-color: #42b883;
    transition: 0.25s ease-in-out;
    border-radius: 5px;
    margin-left: 15px;

    p {
      font-size: 12px;
      color: #fff;
      font-weight: 600;
      margin: 0 0 5px 0;
    }

    &:hover {
      background-color: #2e805b;

      input[type='checkbox'] {
        &:checked {
          & ~ .checkmark {
            background-color: #2e805b;
          }
        }
      }
    }

    input[type='checkbox'] {
      position: absolute;
      opacity: 0;
      cursor: pointer;
      height: 0;
      width: 0;

      &:checked {
        & ~ .checkmark {
          background-color: #42b883;

          &:after {
            display: block;
          }
        }
      }
    }

    :global(.checkmark) {
      height: 18px;
      width: 18px;
      background-color: #fff;
      transition: 0.25s ease-in-out;
      position: relative;
      border-radius: 2px;

      &:after {
        content: '';
        position: absolute;
        display: none;
        left: 3px;
        top: -2px;
        width: 8px;
        height: 13px;
        border: solid #fff;
        border-width: 0 3px 3px 0;
        -webkit-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
        transform: rotate(45deg);
        border-radius: 2px;
      }
    }
  }
</style>
