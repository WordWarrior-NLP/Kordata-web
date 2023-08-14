const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation //get, post, put, delete
    let content_type = 'application/json'
    let body = JSON.stringify(params) // param : 요청 데이터

    let _url = import.meta.env.VITE_SERVER_URL+url //요청 URL
    if(method === 'get') {
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
        method: method,
        headers: {
            "Content-Type": content_type
        }
    }

    if (method !== 'get') {
        options['body'] = body
    }


    /*
    success_callback : API 호출 성공시 수행할 함수, 전달된 함수에는 API 호출시 리턴되는 json이 입력으로 주어진다. 현재 생략	
    failure_callback : API 호출 실패시 수행할 함수, 전달된 함수에는 오류 값이 입력으로 주어진다. 현재 생략
    */
    fetch(_url, options)
        .then(response => {
            response.json()
                .then(json => {
                    if(response.status >= 200 && response.status < 300) {  // 200 ~ 299
                        if(success_callback) {
                            success_callback(json)
                        }
                    }else {
                        if (failure_callback) {
                            failure_callback(json)
                        }else {
                            alert(JSON.stringify(json))
                        }
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        })
}

export default fastapi
