<!-- 사건 노드 정보 -->
<h1 class="mt-4">{event_with_title.name}</h1>
<p><strong>{event_with_title.main_titles[0].title}</strong></p>
<!-- 그래프 넣어야 함 -->
<p>
    Make sure to keep all page content within the
    <code>#page-content-wrapper</code>
    . The top navbar is optional, and just for demonstration. Just create an element with the
    <code>#sidebarToggle</code>
    ID which will toggle the menu when clicked.
</p>

<script>
    export let event_with_title
    console.log(event_with_title.main_titles[0].title)
    // let newest_title = event_with_title.main_titles[0].title    < --- error !! 
</script>