
Kakao.init('b0013f249163dfbf8966b22001d425f1'); 

function shareMessage() {
        Kakao.Share.sendDefault({
            objectType: 'feed',
            content: {
            title: 'You look like...',
            description: '닮은꼴 연예인을 찾아보세요',
            imageUrl:
                'http://k.kakaocdn.net/dn/Q2iNx/btqgeRgV54P/VLdBs9cvyn8BJXB3o7N8UK/kakaolink40_original.png',
            link: {
                // [내 애플리케이션] > [플랫폼] 에서 등록한 사이트 도메인과 일치해야 함
                mobileWebUrl: 'http://127.0.0.1:5501',
                webUrl: 'http://127.0.0.1:5501',
            },
            },
            // social: {
            // likeCount: 286,
            // commentCount: 45,
            // sharedCount: 845,
            // },
            buttons: [
            {
                title: '닮은꼴 연예인 찾으러 가기',
                link: {
                mobileWebUrl: 'http://127.0.0.1:5501/project/mainpage.html',
                webUrl: 'http://127.0.0.1:5501/project/mainpage.html',
                },
            },
            ],
        });
    }

