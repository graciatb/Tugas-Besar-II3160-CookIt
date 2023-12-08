"use client";
import {
  Flex,
  Box,
  Button,
  Heading,
  Text,
  useColorModeValue,
} from "@chakra-ui/react";
import { Card, CardBody } from "@chakra-ui/react";
import PaginationButton from "../component/pagination";
import { useState, useEffect } from "react";
import axios from "../http-axios";
import { useRouter } from "next/navigation";

export default function Recipe() {
  const router = useRouter();
  const [recipes, setRecipes] = useState([]);
  const [page, setPage] = useState(1);
  const [totalPage, setTotalPage] = useState(1);
  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const response = await axios.get("/recipe/", {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token"),
          },
        });
        setRecipes(response.data);
      } catch (error) {
        console.log(error);
      }
    };
    fetchRecipes();
  }, []);
  return (
    <Flex bg={useColorModeValue("white", "gray.800")} h="100vh">
      <Box flex="4" p="5">
        <Flex
          bg="orange.400"
          color="white"
          boxShadow="0px 2px 4px rgba(0, 0, 0, 0.2)"
          w="full"
          h="20"
          mb="5"
        >
          <Flex align="center" pl="10">
            <Heading as="h1" size="lg" fontWeight="bold">
              All Recipe
            </Heading>
          </Flex>
        </Flex>
        {recipes?.map((recipe: any) => (
          <Card key={recipe.product_id} bg="gray.50" h="32" justify="center" p="3">
            <CardBody>
              <Flex justifyContent="space-between">
                <Box>
                  <Text fontSize={"xl"} fontWeight={"bold"} pb="2">
                    {recipe.title}
                  </Text>
                  <Text>{recipe.level}</Text>
                  <Text>{recipe.category}</Text>
                </Box>
                <Button
                  colorScheme="orange"
                  variant="solid"
                  mt="3"
                  as={"a"}
                  href={`/dashboard/${recipe.id}/details`}
                >
                  See Detail
                </Button>
              </Flex>
            </CardBody>
          </Card>
        ))}
        <Flex justifyContent="space-between" mt="5">
          <PaginationButton />
        </Flex>
      </Box>
    </Flex>
  );
}
