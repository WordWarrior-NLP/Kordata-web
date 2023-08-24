<script>
    import { Link } from "svelte-routing"; 
    let heading = "뉴스를 바라보는 새로운 시각"
    let greeting_txt = "Since 2023"
    let main_btn_txt = "Tell Me More" 

</script>

<!-- Masthead-->
<header class="masthead"></header>
<div class="button-box w-100 text-center">
    <Link class="btn btn-primary btn-xl text-uppercase mb-5" to="/events">{main_btn_txt}</Link>
</div>