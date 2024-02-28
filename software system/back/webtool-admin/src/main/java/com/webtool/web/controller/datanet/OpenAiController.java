package com.webtool.web.controller.datanet;

import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;
import javax.servlet.http.HttpServletResponse;
import java.util.concurrent.CompletableFuture;

@RestController
@Api("openAi")
@RequestMapping("/openAi")
public class OpenAiController {


    @GetMapping(value = "/request")
    public SseEmitter request(HttpServletResponse response, @RequestParam String question) {
        return submit(response, question);
    }


    public SseEmitter submit(HttpServletResponse response, String question) {
        SseEmitter emitter = new SseEmitter();
        response.setContentType("text/event-stream;charset=utf-8");
        // Simulate an async process to get the answer to the question
        CompletableFuture.runAsync(() -> {
            try {
                String answerPart = getAnswerPart(question); // Replace this with your actual processing logic
                emitter.send(answerPart);
                Thread.sleep(1000);
                emitter.send("Answer Done!");
                emitter.complete();
            } catch (Exception e) {
                emitter.completeWithError(e);
            }
        });

        return emitter;
    }

    private String getAnswerPart(String question) {
        if (question.contains("地球表层系统")) {
            return "地球表层系统（Earth's Surface System）是一个相互联系的、复杂的自然系统，包括大气、水体、冰川、土壤、生物和岩石等组成部分。这些部分之间的相互作用影响了地球表面的形态、气候、生态系统以及人类社会。地球表层系统研究的目的是为了更好地理解这些相互作用，以便更好地管理和保护我们的环境。<br/>" +
                    "<br/>" +
                    "以下是地球表层系统的一些主要组成部分：<br/>" +
                    "<br/>" +
                    "1.大气：地球的气氛是一个包含氮、氧、氩等气体的混合物。大气影响了地球表面的气候和天气，同时为生物提供了生存所需的气体。<br/>" +
                    "<br/>" +
                    "2.水体：地球表面的水体，包括海洋、湖泊、河流等。水循环过程中的蒸发、降水和径流等现象，对地球表面的气候和生态系统具有重要影响。<br/>" +
                    "<br/>" +
                    "3.冰川：冰川是地球表面的一种重要现象，主要分布在高纬度地区和高海拔山区。冰川对地球的气候、水资源和海平面变化具有重要意义。<br/>" +
                    "<br/>" +
                    "4.土壤：土壤是地球表层的一个组成部分，由矿物质、有机物、水分和气体等组成。土壤对生态系统和农业生产具有重要作用，它们是植物生长的基础，也是水和气体交换的场所。<br/>" +
                    "<br/>" +
                    "5.生物：地球表层的生物是一个复杂的生态系统，包括动植物、微生物等。生物对地球表层系统的物质循环和能量转换过程具有重要作用。<br/>" +
                    "<br/>" +
                    "6.岩石：地球表层的岩石是由矿物质组成的固体物质，如火成岩、沉积岩和变质岩等。岩石的形成、破坏和转化过程对地球表面的形态、水循环和生态系统具有重要影响。<br/>" +
                    "<br/>" +
                    "通过研究这些组成部分，科学家可以更好地理解地球表层系统的运行机制，从而为环境保护和可持续发展提供有力的科学支持。";
        }
        if (question.contains("科学数据网站")) {
            return "地球表层系统开放科学数据网站提供了关于地球表层系统的大量数据。下面是一些知名的地球表层系统开放科学数据网站：<br />" +
                    "<br />" +
                    "1. [NASA Earthdata ↗]https://earthdata.nasa.gov/ 美国国家航空航天局（NASA）提供的地球科学数据，包括大气、陆地表面、海洋和冰川数据。<br />" +
                    "<br />" +
                    "2. [Copernicus Open Access Hub ↗]https://scihub.copernicus.eu/ 欧洲空间局（ESA）提供的Copernicus计划数据。包括地球观测数据、气候变化数据等。<br />" +
                    "<br />" +
                    "3. [National Oceanographic Data Center (NODC) ↗]https://www.nodc.noaa.gov/ 美国国家环境信息中心（NCEI）提供的海洋数据，包括海洋温度、海平面、海底地形等数据。<br />" +
                    "<br />" +
                    "4. [USGS EarthExplorer ↗]https://earthexplorer.usgs.gov/ 美国地质调查局（USGS）提供的地球科学数据，包括地形、地质、土壤、水文等数据。<br />" +
                    "<br />" +
                    "5. [PANGAEA Data Publisher ↗]https://www.pangaea.de/ PANGAEA是一个地球与生命科学领域的开放数据平台，提供地质、地球化学、气候、生态等领域的数据。<br />" +
                    "<br />" +
                    "6. [WorldClim ↗]https://www.worldclim.org/: WorldClim是一个全球气候数据网站，提供了全球的温度、降水、海拔等气候数据。<br />" +
                    "<br />" +
                    "7. [Global Biodiversity Information Facility (GBIF) ↗]https://www.gbif.org/ GBIF提供全球生物多样性数据，包括物种分布、生物群落、生态系统等数据。<br />" +
                    "<br />" +
                    "这些仅是地球表层系统开放科学数据网站的一部分。根据您的研究领域和需求，您可以在这些网站上查找和下载相关数据。";
        }
        if (question.contains("其他")) {
            return "当然，以下是一些其他与地球表层系统相关的开放科学数据网站：<br />" +
                    "<br />" +
                    "1. [European Space Agency Climate Change Initiative (ESA CCI) ↗](https://climate.esa.int/): 欧洲空间局（ESA）的气候变化项目提供了多种气候相关数据，如海洋、大气、冰川等。<br />" +
                    "<br />" +
                    "2. [Global Runoff Data Centre (GRDC) ↗](https://www.bafg.de/GRDC/EN/Home/homepage_node.html): 位于德国的全球径流数据中心（GRDC）提供全球河流径流量数据。<br />" +
                    "<br />" +
                    "3. [The National Snow and Ice Data Center (NSIDC) ↗](https://nsidc.org/): 美国国家雪和冰数据中心（NSIDC）提供了关于全球雪、冰川和冻土的数据。<br />" +
                    "<br />" +
                    "4. [Oak Ridge National Laboratory Distributed Active Archive Center (ORNL DAAC) ↗](https://daac.ornl.gov/): 美国橡树岭国家实验室分布式活动档案中心（ORNL DAAC）提供了关于地球生物圈、大气和水文的数据。<br />" +
                    "<br />" +
                    "5. [Socioeconomic Data and Applications Center (SEDAC) ↗](https://sedac.ciesin.columbia.edu/): 哥伦比亚大学地球研究所（CIESIN）的社会经济数据与应用中心（SEDAC）提供了全球人类活动与环境的数据。<br />" +
                    "<br />" +
                    "6. [World Resources Institute (WRI) ↗](https://www.wri.org/): 世界资源研究所（WRI）提供了关于全球自然资源、环境影响和可持续发展的数据。<br />" +
                    "<br />" +
                    "7. [European Centre for Medium-Range Weather Forecasts (ECMWF) ↗](https://www.ecmwf.int/): 欧洲中期天气预报中心（ECMWF）提供了全球及地区天气预报和再分析数据。<br />" +
                    "<br />" +
                    "以上仅是一部分地球表层系统开放科学数据网站。在这些网站上，您可以找到与地球、气候、生态和社会经济等方面相关的数据。根据您的需求和研究领域，您可以继续探索其他相关数据网站。";
        }
        return "对不起，请换一个问题";
    }

}
