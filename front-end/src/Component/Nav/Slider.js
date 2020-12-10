import { Container } from '@material-ui/core'
import React from 'react'
import { Parallax, Background } from 'react-parallax';
function Slider() {
    return (<div>
        <Container className="top-slider" maxWidth="100%">
            <Parallax
                blur={{ min: -15, max: 15 }}
                bgImage="/images/pyramid.jpg"
                bgImageAlt="the dog"
                strength={-200}
            >

                <div style={{ height: '80vh' }} >
                    <div className="slider-content">
                        <h1 className="slider-title"> KTS Tourism   </h1>

                    </div>
                </div>

            </Parallax>

        </Container>
        

    </div>)
}

export default Slider