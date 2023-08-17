<div class="border-end bg-white d-flex flex-column align-items-stretch flex-shrink-0" id="sidebar-wrapper">
  <div class="sidebar-heading border-bottom bg-light"><span class="fs-5 fw-semibold">Articles</span></div>
  <div class="list-group list-group-flush border-bottom scrollarea">
      {#each days as day, index}
          <a href="#" class="list-group-item list-group-item-action active py-3 lh-tight list-group-item-light" aria-current="true">
              <div class="d-flex w-100 align-items-center justify-content-between">
                  <strong class="mb-1">List group item heading</strong>
                  <small>{index}</small>
              </div>
              <div class="col-10 mb-1 small">Some placeholder content in a paragraph below the heading and date.</div>
          </a>
      {/each}
  </div>
</div>
<script>
  let days = ["sun", 'mon', 'tue', 'wed', 'thu', 'fri', 'sun']
</script>