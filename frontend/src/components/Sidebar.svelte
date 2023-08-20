<div class="border-end bg-white d-flex flex-column align-items-stretch flex-shrink-0" id="sidebar-wrapper">
  <div class="sidebar-heading border-bottom"><span class="fs-5 fw-semibold">Articles</span></div>
  <div class="list-group list-group-flush border-bottom scrollarea">
    {#each news_list as cluster}
      {#each cluster.news as news}
        <a href={news.linkUrl} target="_blank" class="list-group-item list-group-item-action py-3 lh-tight" aria-current="true">
          <div class="col-11 mb-1 small"><strong>{news.title}</strong></div>
          <div class="d-flex w-100 align-items-center justify-content-between">
            <small class="mb-1">{news.pid}</small>
            <small>{cluster.datetime}</small>
          </div>
        </a>  
      {/each}
    {/each}
  </div>
</div>
<script>
  export let news_list;
</script>